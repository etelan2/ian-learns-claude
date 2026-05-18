# Sesión 4 — Cuando Claude se equivoca

**Duración**: 90 minutos
**Entregable**: 3 bugs reales resueltos en tu proyecto
**Meta-aprendizaje**: la AI alucina. La AI miente con confianza. Tú verificas.

---

## Antes de empezar

- [ ] Tu proyecto definido en sesión 3
- [ ] Scaffold creado y subido a GitHub

---

## La realidad de programar con AI

Claude es brillante. Pero también:
- A veces inventa funciones que no existen
- A veces te da código que parece correcto pero no compila
- A veces te asegura algo con confianza que es falso
- A veces te repite el mismo error después de que le dices que está mal

Esto NO es porque sea malo. Es la naturaleza del modelo. La habilidad clave en 2026 es:

> **Verificar lo que la AI te dice antes de confiar en ello.**

Esta sesión la vas a entrenar.

---

## Parte 1 (40 min) — Build con bugs intencionales

Vas a construir tus primeras 1-2 features de tu proyecto.

Pídele a Claude:

```
Quiero empezar a construir [FEATURE 1 de mi scope]. Hazlo conmigo paso a paso. Explícame cada decisión.
```

**Mientras construyes, vas a encontrar bugs.** Es seguro que sí. Cuando uno aparezca:

### Patrón "no funciona"

❌ **Lo que NO debes decir**:
> "No funciona"
> "Está roto"
> "Ayúdame"

✅ **Lo que SÍ debes decir**:
> "Corrí el comando X. Me salió este error textual: [pega el error completo]"
> "Esperaba que pasara A, pero pasó B"

**Diferencia**: en el segundo caso, Claude tiene info real para diagnosticar. En el primero, Claude tiene que adivinar.

---

## Parte 2 (15 min) — Tu sesión de "leer errores"

Cuando salga el primer error real:

1. **No le digas nada a Claude todavía.** Léelo.
2. Identifica:
   - ¿Qué línea?
   - ¿Qué archivo?
   - ¿Qué dice exactamente?
3. Tradúcelo a español mentalmente.
4. Hipótesis: ¿qué crees que está pasando?
5. **Ahora** habla con Claude:

```
Me salió este error: [pega completo]
Estaba ejecutando: [comando]
Mi hipótesis es que [lo que crees].
¿Estás de acuerdo? ¿Qué falta verificar antes de cambiar nada?
```

Esa forma de preguntar = nivel senior. La aprendes hoy.

---

## Parte 3 (15 min) — Cuando Claude se equivoca

En esta sesión va a pasar al menos una vez que Claude te diga algo que NO funcione.

Cuando pase, NO te enojes. Tu trabajo:

```
Hiciste X. Lo intenté. No funcionó. Me salió esto: [error]

¿Qué pasó? ¿Por qué tu sugerencia no funcionó? ¿Qué información te faltaba para darme la solución correcta?
```

**Esa última pregunta es oro.** Claude va a decirte qué información necesitaba. La próxima vez, le das esa info de entrada.

Eso es **prompt engineering en la vida real**. No es una habilidad abstracta. Es saber qué contexto darle a tu colega AI.

---

## Parte 4 (15 min) — Documentar tus bugs

Crea un archivo `bitacora/bugs-aprendidos.md`. Para cada bug que resolviste en esta sesión:

```markdown
## Bug N: [descripción de 1 línea]
- **Qué pasaba**: [síntoma]
- **Qué intenté primero**: [tu primera hipótesis]
- **Cuál era el problema real**: [la causa)
- **Cómo lo arreglé**: [solución]
- **Lección**: [qué aprendí]
```

Mínimo 3 bugs documentados. Si no te salieron 3, no estás programando suficiente. Sigue.

Commit + push.

---

## Parte 5 (5 min) — Bitácora

`bitacora/sesion-4.md`:

1. Qué aprendí hoy
2. Qué me costó
3. Qué quiero hacer la próxima
4. **Bonus**: ¿en qué momento Claude se equivocó? Cuéntalo en 2 frases.

---

## Meta-lección

> Programar no es escribir código que funcione. Es saber qué hacer cuando NO funciona.

El 70% del tiempo de un programador profesional es debugging. La AI lo aceleró pero no lo eliminó. Lo que cambió es:
- Antes: leer Stack Overflow durante horas
- Ahora: conversar con tu AI sobre el bug, verificando

La gente que sabe verificar lo que la AI dice va a ganar el doble que la que no. Hoy empezaste a practicarlo.

— Federico + Claude
