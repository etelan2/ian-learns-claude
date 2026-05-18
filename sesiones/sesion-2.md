# Sesión 2 — Tu propio repo en el mundo

**Duración**: 90 minutos
**Entregable**: cuenta de GitHub + tu primer repo público + README escrito por ti
**Meta-aprendizaje**: lo que escribes en código existe permanentemente. Git es tu memoria.

---

## Antes de empezar

- [ ] Sesión 1 completada
- [ ] Tu hola.py funcionando
- [ ] Bitácora de sesión 1 escrita

---

## Parte 1 (15 min) — Crear cuenta GitHub

GitHub es donde vive el código del mundo. Linux, Python, Claude Code, todo está en GitHub.

1. Ve a **github.com**
2. Sign up con tu correo
3. Tu username: piensa bien — va a ser tu identidad como programador para siempre. Sugerencia: `ian-pa` o `ianperez` (lo que sea TU nombre real, no algo random). NO uses números si puedes evitarlo.
4. Confirma correo

**Una vez dentro**: pídele a Claude:

```
Acabo de crear mi cuenta de GitHub. Mi username es [TU_USERNAME]. ¿Qué es GitHub y por qué importa que tenga una cuenta?
```

Lee la respuesta.

---

## Parte 2 (20 min) — Instalar git en tu Mac

Probablemente ya viene instalado. Pídele a Claude:

```
¿Cómo verifico si git está instalado en mi Mac? Si no está, ¿cómo lo instalo?
```

Sigue sus instrucciones paso por paso. Cuando termines, pídele:

```
¿Cómo conecto mi git local con mi cuenta de GitHub? Mi username es [TU_USERNAME] y mi correo es [TU_CORREO].
```

---

## Parte 3 (30 min) — Tu primer repo

Pídele a Claude:

```
Quiero crear un repo en GitHub que se llame "ian-aprende-claude". Va a ser donde guardo todo lo que aprendo en este curso. ¿Cómo lo hago paso a paso?
```

Va a guiarte por:
1. Crear el repo en github.com (botón verde "New")
2. Hacer `git clone` en tu Mac para tenerlo local
3. Mover tu `hola.py` adentro
4. Hacer `git add`, `git commit`, `git push`

**Cuando hagas push y veas tu código en GitHub.com → ese es el momento clave.** Tu código está en internet. Es público. Es tuyo.

---

## Parte 4 (20 min) — README en markdown

Todo repo serio tiene un README. Es la portada.

Pídele a Claude:

```
Quiero escribir un README para mi repo. ¿Qué es markdown? ¿Cómo funciona? Dame ejemplos cortos.
```

Practica con él. Aprende:
- `# Título grande`
- `## Subtítulo`
- `**negritas**`
- `- listas`
- `[enlace](https://...)`
- ` ```bloque de código``` `

Crea tu README. Pídele a Claude que te ayude pero TÚ escribes el contenido. Debe responder:
- ¿Quién eres?
- ¿Qué es este repo?
- ¿Por qué estás aprendiendo?

Hazlo personal. No copies plantillas genéricas. **Tu README es tu carta de presentación al mundo programador.**

Haz commit + push.

---

## Parte 5 (5 min) — Bitácora

Abre `bitacora/sesion-2.md` (créalo si no existe):

1. Qué aprendí hoy
2. Qué me costó
3. Qué quiero hacer la próxima

Commit + push. **Tu bitácora también está en GitHub ahora.**

---

## Meta-lección

> Git es la única herramienta que han usado todos los programadores del mundo durante los últimos 20 años. Vas a usarla todos los días el resto de tu vida si te dedicas a esto.

No necesitas dominarla ahora. Solo familiarizarte. Las cosas que vamos a usar 100 veces más:
- `git add .` (agregar cambios)
- `git commit -m "mensaje"` (guardarlos)
- `git push` (subirlos al mundo)
- `git pull` (bajar cambios del mundo)

Los aprendes con el cuerpo, no con la cabeza. En 4 sesiones más los harás sin pensar.

— Federico + Claude
