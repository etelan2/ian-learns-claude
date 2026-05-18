# Sesión 3 — Tu primer proyecto real

**Duración**: 90 minutos
**Entregable**: definir tu proyecto + scaffold funcionando local
**Meta-aprendizaje**: definir scope = la habilidad más importante del programador.

---

## La sesión más importante del curso

Esta sesión es la más importante. Porque vas a decidir **qué vas a construir durante las próximas 5 sesiones**. Si eliges algo aburrido o demasiado grande, vas a sufrir. Si eliges algo bueno, te vas a obsesionar y vas a aprender el triple.

---

## Parte 1 (30 min) — Brainstorming con Claude

Habla con Claude. Empieza así:

```
Quiero construir un proyecto de software durante las próximas 5 sesiones. Soy nuevo, sé Python básico, recién terminé las primeras 2 sesiones del curso.

Antes de proponerme ideas, hazme 5 preguntas para conocerme:
- Qué me gusta hacer en mi tiempo libre
- Qué cosa me frustra del mundo o de mi día a día
- Qué he visto en internet que pensé "yo podría hacer algo así"
- Qué app o herramienta uso todos los días que podría ser mejor
- A quién le gustaría que mi proyecto le sirva (mi mamá, mis amigos, gente desconocida, yo mismo)

Hazme las preguntas de una en una, escucha mis respuestas, y después propón 3 proyectos.
```

Responde con sinceridad. **No digas lo que crees que Claude quiere oír. Di lo que realmente piensas.**

---

## Parte 2 (15 min) — Elegir tu proyecto

Claude te va a proponer 3 ideas. Léelas con calma.

Por cada idea, pregúntate:
- ¿Esto me daría ganas de trabajar en eso fuera de las sesiones?
- ¿Esto lo entendería mi mamá si se lo explico?
- ¿Esto cabe en 5 sesiones de 90 min cada una?

Si ninguna te late, pídele:

```
Ninguna de estas me convence al 100%. Aquí está qué me gusta más / menos de cada una. Propón 3 más.
```

Itera hasta que UNA te emocione.

**Reglas para no equivocarte**:
- ❌ NO elijas algo solo porque suena impresionante
- ❌ NO elijas algo que ya existe igualito
- ❌ NO elijas algo "para hacerte rico"
- ✅ Elige algo que TÚ querrías usar
- ✅ Elige algo que se pueda terminar
- ✅ Elige algo que puedas mostrar en una sola pantalla

---

## Parte 3 (15 min) — Definir el scope

Una vez elegido, pídele:

```
Quiero definir el scope MÍNIMO de este proyecto. Quiero algo que funcione en 5 sesiones, no algo perfecto.

Ayúdame a contestar:
1. ¿Qué hace exactamente este proyecto? (en una frase)
2. ¿Para quién? (una persona específica, no "todo el mundo")
3. ¿Cuáles son las 3 features mínimas que tiene que tener?
4. ¿Qué NO va a tener? (lo difícil)
5. ¿En qué pantalla vive? (web, terminal, app móvil, etc.)
```

**El truco**: la lista de "qué NO va a tener" es más importante que la lista de features. Escríbela bien.

---

## Parte 4 (20 min) — Scaffold

Pídele:

```
Vamos a hacer el scaffold inicial (estructura de carpetas, archivos vacíos) de este proyecto. NO escribas código todavía — solo la estructura.

¿Qué tecnologías propones? ¿Por qué? Explícame las opciones antes de elegir.
```

Aprende a elegir tecnología. Lo más importante en este curso.

Cuando tengan el plan claro:

```
Crea el scaffold en una carpeta nueva dentro de proyectos/. Hazlo paso a paso, explicándome qué hace cada archivo.
```

Cuando termines:

```bash
git add proyectos/
git commit -m "Sesión 3: scaffold de [NOMBRE DE TU PROYECTO]"
git push
```

---

## Parte 5 (10 min) — Bitácora

`bitacora/sesion-3.md`:

1. **Qué aprendí hoy**:
2. **Qué me costó**:
3. **Qué quiero hacer la próxima**:
4. **Mi proyecto se llama**: _______
5. **Hace**: _______
6. **Para**: _______

Commit + push.

---

## Meta-lección

> El 90% de los proyectos de software fallan no porque la tecnología sea mala, sino porque nunca se definió bien qué iban a ser.

Las preguntas que contestaste hoy (1-5 del scope) son **literalmente las mismas que hacen los founders de billones de dólares** antes de empezar.

No memorices código. Memoriza este proceso.

— Federico + Claude
