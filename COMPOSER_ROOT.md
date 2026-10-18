# composer.json (raíz del repo) — por qué existe

**Packagist solo indexa un `composer.json` en la RAÍZ del repositorio**: no
acepta subdirectorios ni rutas (`POST /api/create-package` solo recibe
`{"repository": "<url del repo>"}`, sin campo de subpath). El SDK PHP vive en
`sdks/php/`, así que este fichero es su manifiesto de publicación: replica los
campos de `sdks/php/composer.json` con las rutas remapeadas al subdirectorio
(`autoload` → `sdks/php/`).

**La versión NO se escribe aquí**: composer la deriva del **tag git de la raíz**
del repositorio (de ahí que el release se etiquete `v0.4.1` y no
`sdks/php/v0.4.1`).

**Regla de sincronía**: los dos manifiestos describen el MISMO paquete. Los
campos `name`, `license`, `type`, `require`, `keywords`, `homepage`, `support`
y `authors` deben ser idénticos; solo cambian las rutas. La suite
`bash cli.sh test b4n1-boost` lo verifica (sección "manifiestos del espejo"),
porque un `composer.json` de raíz desincronizado publicaría un paquete que no
es el del repositorio privado.
