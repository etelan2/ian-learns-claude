# Sesión 6 — Deploy

**Duración**: 90 minutos
**Entregable**: tu proyecto LIVE en internet, con URL pública
**Meta-aprendizaje**: tu trabajo puede ser usado por humanos reales.

---

## Antes de empezar

- [ ] Tu proyecto funciona local con integración (sesión 5)
- [ ] Subido a GitHub

---

## El día que tu proyecto sale al mundo

Hasta hoy, solo tú podías usar tu proyecto (porque corre en tu Mac). Hoy lo vas a poner en internet. Cualquier persona en el mundo va a poder abrir tu URL y usarlo.

Eso es **deploy**. Es el momento donde dejas de ser "alguien que aprende a programar" y empiezas a ser "alguien que construye cosas para gente real".

---

## Parte 1 (15 min) — Elegir dónde deploy

Pídele a Claude:

```
Mi proyecto está en [Python/Node/etc.] y hace [X]. Quiero hacer deploy.

Las opciones más fáciles que conozco son:
- Vercel
- Cloudflare Pages
- Render
- Railway
- GitHub Pages

Para MI proyecto específico, ¿cuál es la mejor opción? Comparemos pros y contras de las 2 más relevantes para mi caso.
```

Lee. Decide.

---

## Parte 2 (40 min) — Hacer el deploy

Pídele:

```
Vamos a hacer deploy en [plataforma elegida]. Hazlo paso a paso. Avísame antes de cada paso porque quiero entender qué pasa.
```

Va a pasar (es normal):
- Te va a pedir crear cuenta en la plataforma
- Te va a pedir conectar tu GitHub
- Te va a pedir configurar variables de ambiente (los `.env` que aprendiste en sesión 5)
- Va a haber al menos un error en el primer intento

**Cuando falle**: revisa los logs. Pídele a Claude:

```
El deploy falló. Aquí están los logs: [pega completos]
¿Qué pasó? ¿Qué hay que cambiar?
```

Itera hasta que funcione.

---

## Parte 3 (15 min) — Compartir tu URL

Cuando tengas tu URL pública funcionando:

1. **Abre tu proyecto desde el teléfono** (no desde tu Mac). Si funciona ahí también, está real.
2. **Compártela con 3 personas**:
   - Federico (obvio)
   - Tu mamá
   - Un amigo
3. Pídeles que la usen. Que te digan qué piensan.

**Documenta el primer feedback que recibas.** Aunque sea malo. Va a ser información valiosa.

---

## Parte 4 (15 min) — Monitoreo básico

Pregúntale:

```
Mi proyecto ya está en internet. ¿Cómo sé si está funcionando? ¿Qué pasa si se cae? ¿Cómo me entero?

Configúrame algo simple para saber el estado de mi proyecto sin tener que abrirlo cada rato.
```

Aprende sobre uptime monitoring (gratis con UptimeRobot o similar). Configúralo.

---

## Parte 5 (5 min) — Bitácora

`bitacora/sesion-6.md`:

1. Qué aprendí hoy
2. Qué me costó
3. **Mi URL pública**: _______
4. **Primer feedback que recibí**: _______
5. **Qué cambiaría a partir del feedback**: _______

Commit + push.

**Bonus**: agrega un badge a tu README con tu URL deployed:

```markdown
🌐 **Live**: [TU_URL_AQUÍ](https://...)
```

---

## Meta-lección

> Hasta que la gente real lo use, no es producto. Es ejercicio.

Hoy fue el día más importante del curso. La gente que terminó la sesión 6 está en otro nivel que la gente que solo "aprendió Python".

— Federico + Claude
