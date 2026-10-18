<?php

// B4N1-Boost PHP SDK — Business Source License 1.1 (BUSL-1.1).
// Thin FFI wrapper over the proprietary B4N1 native core.
// The native binary is licensed separately under the B4N1 EULA (EULA.txt).
// Copyright (c) 2026 B4N1. All rights reserved.

namespace B4N1;

use FFI;

class Boost {
    private static ?FFI $ffi = null;

    private static function init(): void {
        if (self::$ffi !== null) return;

        $envPath = getenv('B4N1_BOOST_LIB_PATH');
        if ($envPath !== false && $envPath !== '') {
            $real = realpath($envPath) ?: $envPath;
            if (!str_ends_with($real, 'libb4n1_boost.so') && !str_ends_with($real, 'libb4n1_boost.dylib') && !str_ends_with($real, 'b4n1_boost.dll')) {
                throw new \InvalidArgumentException("Invalid library filename in B4N1_BOOST_LIB_PATH");
            }
            $libPath = $real;
        } else {
            $arch = strtolower(php_uname('m'));
            switch (PHP_OS_FAMILY) {
                case 'Linux':
                    $slug = in_array($arch, ['aarch64', 'arm64'], true) ? 'linux-arm64' : 'linux-x64';
                    $name = 'libb4n1_boost.so';
                    break;
                case 'Darwin':
                    $slug = in_array($arch, ['aarch64', 'arm64'], true) ? 'macos-arm64' : 'macos-x64';
                    $name = 'libb4n1_boost.dylib';
                    break;
                case 'Windows':
                    $slug = 'windows-x64';
                    $name = 'b4n1_boost.dll';
                    break;
                default:
                    throw new \RuntimeException('Unsupported platform for b4n1-boost: ' . PHP_OS_FAMILY . '/' . $arch);
            }
            // 1) Native lib bundled in the composer package (native/<platform>/).
            $bundled = __DIR__ . '/native/' . $slug . '/' . $name;
            // 2) Development fallback (running from the source repo).
            $dev = __DIR__ . '/../../target/release/' . $name;
            if (is_file($bundled)) {
                $libPath = $bundled;
            } elseif (is_file($dev)) {
                $libPath = $dev;
            } else {
                throw new \RuntimeException(
                    "b4n1-boost native library not found. Looked at {$bundled} and {$dev}. "
                    . 'Set B4N1_BOOST_LIB_PATH or reinstall the package.'
                );
            }
        }

        
        $cdef = "
            int32_t b4n1_boost_compress_gzip(const char* data, size_t len, uint8_t** out_ptr, size_t* out_len, uint32_t level);
            int32_t b4n1_boost_compress_zstd(const char* data, size_t len, uint8_t** out_ptr, size_t* out_len, int32_t level);
            int32_t b4n1_boost_decompress_zstd(const char* data, size_t len, uint8_t** out_ptr, size_t* out_len);
            void b4n1_boost_free_buffer(uint8_t* ptr, size_t len);
            char* b4n1_boost_minify_html(const char* input);
            int32_t b4n1_boost_json_validate(const char* input);
            void b4n1_boost_free_string(char* ptr);
        ";

        self::$ffi = FFI::cdef($cdef, $libPath);
    }

    public static function compressGzip(string $data, int $level = 4): string {
        self::init();
        $len = strlen($data);
        if ($len === 0) return "";

        $outPtr = self::$ffi->new("uint8_t*");
        $outLen = self::$ffi->new("size_t");

        $res = self::$ffi->b4n1_boost_compress_gzip($data, $len, FFI::addr($outPtr), FFI::addr($outLen), $level);
        if ($res !== 0) {
            throw new \RuntimeException("Gzip compression failed");
        }

        $result = FFI::string($outPtr, $outLen->cdata);
        self::$ffi->b4n1_boost_free_buffer($outPtr, $outLen->cdata);
        return $result;
    }

    public static function compressZstd(string $data, int $level = 3): string {
        self::init();
        $len = strlen($data);
        if ($len === 0) return "";

        $outPtr = self::$ffi->new("uint8_t*");
        $outLen = self::$ffi->new("size_t");

        $res = self::$ffi->b4n1_boost_compress_zstd($data, $len, FFI::addr($outPtr), FFI::addr($outLen), $level);
        if ($res !== 0) {
            throw new \RuntimeException("Zstd compression failed");
        }

        $result = FFI::string($outPtr, $outLen->cdata);
        self::$ffi->b4n1_boost_free_buffer($outPtr, $outLen->cdata);
        return $result;
    }

    public static function minifyHtml(string $html): string {
        self::init();
        $outStr = self::$ffi->b4n1_boost_minify_html($html);
        if ($outStr === null) return $html;

        $result = FFI::string($outStr);
        self::$ffi->b4n1_boost_free_string($outStr);
        return $result;
    }

    public static function isJsonValid(string $json): bool {
        self::init();
        return self::$ffi->b4n1_boost_json_validate($json) === 1;
    }
}
