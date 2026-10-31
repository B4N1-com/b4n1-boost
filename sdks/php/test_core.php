<?php
// Core-primitives contract tests for the PHP b4n1-boost SDK (cache/bloom/
// breaker). Required by test.php — shares its check() + counters so the
// final [CORE] summary covers the whole suite.
require_once __DIR__ . '/Core.php';

use B4N1\Boost\ResponseCache;
use B4N1\Boost\BloomFilter;
use B4N1\Boost\CircuitBreaker;

// ── Response cache ─────────────────────────────────────────────────────────

$c = new ResponseCache(8);
$c->set('user:1', '{"id":1}', 200, 60);
$hit = $c->get('user:1');
check('cache: set + get round-trip', $hit !== null && $hit['body'] === '{"id":1}' && $hit['status'] === 200);
check('cache: miss returns null', $c->get('nope') === null);
$c->set('k', 'x', 201, 60);
check('cache: custom status preserved', $c->get('k')['status'] === 201);
$c->set('k', 'old', 200, 60);
$c->set('k', 'new', 201, 60);
$hit = $c->get('k');
check('cache: overwrite updates value and status', $hit['body'] === 'new' && $hit['status'] === 201);
$c->set('never', 'x', 204, 0);
check('cache: TTL=0 never expires', $c->get('never') !== null);
$c->clear();
check('cache: clear removes all entries', $c->get('user:1') === null && $c->get('k') === null);
$c->set('k', 'x', 200, 60);
check('cache: invalidate existing returns true', $c->invalidate('k') === true && $c->get('k') === null);
check('cache: invalidate nonexistent returns false', $c->invalidate('nope') === false);
$c->set('bin', hex2bin('00ff10'), 200, 60);
check('cache: binary-safe body', $c->get('bin')['body'] === hex2bin('00ff10'));
$c->close();
$c->close(); // idempotent
check('cache: get after close declined (State 2)', $c->get('k') === null);

$threw = false;
try {
    new ResponseCache(2000000);
} catch (\InvalidArgumentException $e) {
    $threw = true;
}
check('cache: oversized capacity rejected (State 2)', $threw);

// ── Bloom filter ───────────────────────────────────────────────────────────

$b = new BloomFilter(1000, 0.01);
check('bloom: first sight is new (false)', $b->checkAndSet('user-1') === false);
check('bloom: second sight is duplicate (true)', $b->checkAndSet('user-1') === true);
check('bloom: different items are independent', $b->checkAndSet('a') === false && $b->checkAndSet('b') === false && $b->checkAndSet('a') === true);
$b->close();
$b->close();
check('bloom: check after close declined (State 2)', $b->checkAndSet('x') === false);

$threw = false;
try {
    new BloomFilter(20000000, 0.01);
} catch (\InvalidArgumentException $e) {
    $threw = true;
}
check('bloom: oversized items rejected (State 2)', $threw);

// ── Circuit breaker ────────────────────────────────────────────────────────

$cb = new CircuitBreaker(2, 1, 60);
check('circuit: starts closed (allows)', $cb->allows() === true);
$cb->recordFailure();
check('circuit: one failure stays closed', $cb->allows() === true);
$cb->recordFailure();
check('circuit: opens after threshold failures', $cb->allows() === false);
$cb2 = new CircuitBreaker(2, 1, 60);
$cb2->recordSuccess();
$cb2->recordSuccess();
$cb2->recordFailure();
check('circuit: success keeps it closed', $cb2->allows() === true);
$cb2->close();
check('circuit: invalid handle fails closed (State 2)', $cb2->allows() === false);
$cb->close();
