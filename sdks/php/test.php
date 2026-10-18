<?php

require_once __DIR__ . '/Boost.php';
require_once __DIR__ . '/Middleware.php';

use B4N1\Boost;
use B4N1\Boost\BoostMiddleware;

$passed = 0;
$failed = 0;

function check(string $name, bool $ok): void {
    global $passed, $failed;
    if ($ok) {
        echo "  ✓ $name\n";
        $passed++;
    } else {
        echo "  ✗ $name\n";
        $failed++;
    }
}

echo "[TEST] Running comprehensive PHP b4n1-boost SDK tests...\n\n";

// ── State 1: Exists & Correct ─────────────────────────────────────────────

check('json: valid object', Boost::isJsonValid('{"a":1}') === true);
check('json: valid array', Boost::isJsonValid('[1,2,3]') === true);
check('json: valid string', Boost::isJsonValid('"hello"') === true);
check('json: valid null', Boost::isJsonValid('null') === true);
check('json: valid true', Boost::isJsonValid('true') === true);
check('json: valid false', Boost::isJsonValid('false') === true);
check('json: valid number', Boost::isJsonValid('42') === true);
check('json: valid negative float', Boost::isJsonValid('-3.14') === true);
check('json: valid nested', Boost::isJsonValid('{"a":{"b":[1,2,{"c":null}]}}') === true);
check('json: valid unicode escape', Boost::isJsonValid('"hello \u00e9"') === true);
check('json: valid empty object', Boost::isJsonValid('{}') === true);
check('json: valid empty array', Boost::isJsonValid('[]') === true);

// ── State 2: Exists & Incorrect ───────────────────────────────────────────

check('json: invalid empty', Boost::isJsonValid('') === false);
check('json: invalid brace', Boost::isJsonValid('{') === false);
check('json: invalid bracket', Boost::isJsonValid(']') === false);
check('json: invalid trailing comma', Boost::isJsonValid('[1,]') === false);
check('json: invalid unquoted key', Boost::isJsonValid('{a:1}') === false);
check('json: invalid single quotes', Boost::isJsonValid("{'a':1}") === false);
check('json: invalid undefined', Boost::isJsonValid('undefined') === false);
check('json: invalid NaN', Boost::isJsonValid('NaN') === false);
check('json: invalid leading zero', Boost::isJsonValid('01') === false);
check('json: invalid bare string', Boost::isJsonValid('hello') === false);

// ── Compression: gzip ─────────────────────────────────────────────────────

$payload = str_repeat('Hello, World! ', 100);
$gz = Boost::compressGzip($payload, 6);
check('gzip: compressed is smaller', strlen($gz) > 0 && strlen($gz) < strlen($payload));
$decoded = gzdecode($gz);
check('gzip: round-trip', $decoded === $payload);

$large = str_repeat('x', 100000);
$largeGz = Boost::compressGzip($large, 4);
check('gzip: large payload compresses well', strlen($largeGz) < 1000);
check('gzip: large round-trip', gzdecode($largeGz) === $large);

for ($level = 1; $level <= 9; $level += 2) {
    $c = Boost::compressGzip($payload, $level);
    check("gzip: level $level round-trip", gzdecode($c) === $payload);
}

// ── Compression: zstd ─────────────────────────────────────────────────────

$zs = Boost::compressZstd($payload, 3);
check('zstd: compressed is smaller', strlen($zs) > 0 && strlen($zs) < strlen($payload));

$largeZs = Boost::compressZstd($large, 3);
check('zstd: large payload compresses well', strlen($largeZs) < 100);

for ($level = 1; $level <= 19; $level += 4) {
    $c = Boost::compressZstd($payload, $level);
    check("zstd: level $level produces output", strlen($c) > 0);
}

// ── HTML minification ─────────────────────────────────────────────────────

$raw = '<div>   <h1>  Title  </h1>   <p>  Body  </p>  </div>';
$min = Boost::minifyHtml($raw);
check('minify: collapses whitespace', strlen($min) < strlen($raw) && !str_contains($min, '   '));
check('minify: preserves content', str_contains($min, 'Title') && str_contains($min, 'Body'));
check('minify: empty string', Boost::minifyHtml('') === '');
check('minify: already minified unchanged', Boost::minifyHtml('<div><p>x</p></div>') === '<div><p>x</p></div>');

// ── Middleware ────────────────────────────────────────────────────────────

// Simple PSR-7-like mock
class MockResponse {
    private string $content;
    public MockHeaderBag $headers;
    public function __construct() { $this->headers = new MockHeaderBag(); }
    public function getContent(): string { return $this->content; }
    public function setContent(string $c): void { $this->content = $c; }
}

class MockHeaderBag {
    private array $headers = [];
    public function get(string $k, string $d = ''): string { return $this->headers[$k] ?? $d; }
    public function set(string $k, string $v): void { $this->headers[$k] = $v; }
}

class MockRequest {
    private array $headers = [];
    public function header(string $k, string $d = ''): string { return $this->headers[$k] ?? $d; }
    public function setHeader(string $k, string $v): void { $this->headers[$k] = $v; }
}

// Minify HTML via middleware
$resp = new MockResponse();
$resp->setContent('<div>   <p>  Hello  </p>  </div>');
$resp->headers->set('Content-Type', 'text/html');
$req = new MockRequest();
$mw = new BoostMiddleware(true, 4);
$mw->handle($req, function($req) use ($resp) { return $resp; });
check('middleware: minifies HTML', !str_contains($resp->getContent(), '   '));

// Gzip compress via middleware
$resp2 = new MockResponse();
$resp2->setContent('<p>Hello</p>');
$resp2->headers->set('Content-Type', 'text/html');
$req2 = new MockRequest();
$req2->setHeader('Accept-Encoding', 'gzip');
$mw2 = new BoostMiddleware(false, 4);
$mw2->handle($req2, function($req) use ($resp2) { return $resp2; });
check('middleware: sets gzip encoding', $resp2->headers->get('Content-Encoding') === 'gzip');
check('middleware: content is gzipped', strlen($resp2->getContent()) < strlen('<p>Hello</p>') || gzdecode($resp2->getContent()) === '<p>Hello</p>');

// ── State 3: Security (path traversal rejection) ──────────────────────────

try {
    putenv("B4N1_BOOST_LIB_PATH=/tmp/malicious/libfake.so");
    $ref = new ReflectionClass(Boost::class);
    $prop = $ref->getProperty('ffi');
    $prop->setAccessible(true);
    $prop->setValue(null, null);
    $method = $ref->getMethod('init');
    $method->setAccessible(true);
    $method->invoke(null);
    check('security: path traversal rejected', false);
} catch (\InvalidArgumentException $e) {
    check('security: path traversal rejected', str_contains($e->getMessage(), 'Invalid library filename'));
} finally {
    putenv("B4N1_BOOST_LIB_PATH");
    $prop->setValue(null, null);
    $method->invoke(null);
}

// ── State 4: Correctly absent ─────────────────────────────────────────────

check('absent: nonExistentMethodXyz not defined', method_exists(Boost::class, 'nonExistentMethodXyz') === false);

// ── Summary ───────────────────────────────────────────────────────────────

echo "\n";
echo "[CORE] $passed passed, $failed failed\n";
if ($failed > 0) exit(1);
