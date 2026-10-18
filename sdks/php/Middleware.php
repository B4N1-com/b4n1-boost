<?php

namespace B4N1\Boost;

/**
 * PSR-7 / PSR-15 / Laravel Compatible Middleware for HTML minification and Gzip compression.
 */
class BoostMiddleware
{
    private bool $minifyHtml;
    private int $gzipLevel;

    public function __construct(bool $minifyHtml = true, int $gzipLevel = 4)
    {
        $this->minifyHtml = $minifyHtml;
        $this->gzipLevel = $gzipLevel;
    }

    /**
     * Handle an incoming HTTP request (Laravel / PSR-15 style).
     */
    public function handle($request, \Closure $next)
    {
        $response = $next($request);

        $content = $response->getContent();
        $contentType = $response->headers->get('Content-Type', '');

        // Minify HTML if HTML content
        if ($this->minifyHtml && str_contains($contentType, 'text/html')) {
            try {
                $minified = \B4N1\Boost::minifyHtml($content);
                if (!empty($minified)) {
                    $content = $minified;
                }
            } catch (\Throwable $e) {
                // Fail-safe: keep original
            }
        }

        // Compress Gzip if client supports it
        $acceptEncoding = $request->header('Accept-Encoding', '');
        if (str_contains($acceptEncoding, 'gzip')) {
            try {
                $compressed = \B4N1\Boost::compressGzip($content, $this->gzipLevel);
                if (!empty($compressed)) {
                    $response->setContent($compressed);
                    $response->headers->set('Content-Encoding', 'gzip');
                    $response->headers->set('Content-Length', (string)strlen($compressed));
                    return $response;
                }
            } catch (\Throwable $e) {
                // Fallback
            }
        }

        $response->setContent($content);
        return $response;
    }
}
