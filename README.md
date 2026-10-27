# TechStore U4 — Implementación del Núcleo de Negocio

## Datos de identificación
* **Actividad:** Actividad 4 - Implementación del núcleo de negocio TechStore
* **Materia:** Componentes de Lógica de Negocios
* **Unidad:** 4
* **Equipo:** 14
* **Integrantes:** 
  * Pedro Omar Cardona Alvarez — Matrícula 2226579
  * Kloudenn Jafed Jiménez Valdivieso — Matrícula 2226639
  * Leonardo Acosta Morales — Matrícula 2226717

## Empresa
**TechStore** es un programa para administrar los pedidos de una tienda ficticia. El sistema convierte registros CSV en objetos de dominio, aplica reglas de descuentos mediante el *Specification Pattern*, controla el ciclo de vida de cada pedido a través de una Máquina de Estados, y ofrece estas operaciones de forma segura mediante una API REST.

## Alcance
El proyecto contiene la implementación técnica de las Entidades y Value Objects (*Domain-Driven Design*), la validación estricta de invariantes (límite de unidades y transiciones de estado), la emisión de Eventos de Dominio, un servicio web construido con FastAPI y una suite de pruebas automatizadas con `pytest`. Al operar en memoria, los cambios no requieren persistencia en base de datos.

## Estructura del proyecto
* `/app`: Contiene el núcleo del dominio, especificaciones y controladores de la API.
* `/tests`: Suite de pruebas unitarias y de integración para validar las reglas y endpoints.
* `/datos`: Archivos CSV de catálogo (clientes, productos, pedidos).
* `/docs`: Archivos pdf de la bitacora el reporte con todo adjuntado
