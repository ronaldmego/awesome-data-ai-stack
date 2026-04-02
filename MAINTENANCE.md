# MAINTENANCE.md — awesome-data-ai-stack

Guía operativa para mantener la lista actualizada.

## Actualizar star counts

El script `scripts/update_stars.py` consulta la GitHub API e inyecta el número de estrellas inline en el README (formato `⭐ 12.4k`). Es idempotente — si ya hay un badge lo sobreescribe.

```bash
cd /home/adminmgo/projects/sites/awesome-data-ai-stack
source ~/.secrets/.env
python3 scripts/update_stars.py --readme README.md --token "$GITHUB_PERSONAL_ACCESS_TOKEN"
git add README.md
git commit -m "chore: refresh star counts"
git push
```

**Token:** `GITHUB_PERSONAL_ACCESS_TOKEN` en `~/.secrets/.env`
**Rate limit autenticado:** 5000 req/hora (suficiente para toda la lista en ~30 seg)
**Frecuencia recomendada:** mensual o al agregar muchos repos nuevos

---

## Agregar nuevos repos

Reglas de oro:
1. **Un repo = una sección.** Nunca repetir el mismo repo en dos categorías.
2. **Formato estándar:**
   ```
   - [owner/repo](https://github.com/owner/repo) - Descripción corta en inglés
   ```
3. **Verificar duplicados antes de agregar:**
   ```bash
   grep "owner/repo" README.md
   ```
4. **Después de agregar**, correr el script de stars para incluir el badge del nuevo repo.

---

## Verificar duplicados

```bash
grep "^- \[" README.md \
  | sed 's/.*(\(https:\/\/github.com\/[^)]*\)).*/\1/' \
  | sort | uniq -d
```

Si hay output → hay duplicados. Decidir en qué sección queda y eliminar el resto.

---

## Estructura de secciones

| Sección | Qué va aquí |
|---------|-------------|
| 🤖 AI Agents & Frameworks | Frameworks de agentes, multi-agent, personal AI |
| 🧩 MCP Servers & Skills | Servidores MCP, skills, plugins |
| 🔀 Orchestration & Multi-Agent | Orchestrators, workflows agénticos |
| 🧠 Memory & RAG | Memoria para agentes, RAG, vector stores |
| 🏛️ Data Governance & Observability | Metadata, lineage, data quality |
| 🛡️ AI Safety & Responsible AI | Guardrails, fairness, eval |
| 🎨 Avatar, Video & Image AI | Generación de multimedia con IA |
| 📊 Data Engineering & Analytics | Pipelines, BI, SQL tools, data platforms |
| 🧠 ML & Data Science | Librerías ML/DL de producción (NO tutoriales) |
| 🛠️ DevTools & Infrastructure | Dev tools, self-hosting, infra |
| 🌐 Web & Apps | Apps web, dashboards, generadores |
| 📚 Learning & Reference | Cursos, tutoriales, awesome lists de referencia |
| 🔍 OCR & Document Processing | Extracción de texto, document AI |
| 📝 Content & Productivity | Productividad, content tools |

**Regla Learning & Reference:** Solo va material educativo (cursos, tutoriales). Las librerías de producción van en su sección técnica correspondiente aunque tengan tutoriales.
