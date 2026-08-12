## Avance semana 1: se midieron 5 operaciones

## Conclusiones

### Recomendaciones de mejora

1. **Completar y mantener actualizado `datos/tiempos.csv`**: en la semana 1 se registraron 5 operaciones, pero el archivo aún no concentra todas las mediciones por estación. Registrar cada operación con `estacion`, `operacion` y `tiempo_seg` permitirá ejecutar `analisis.py` y comparar promedios reales entre estaciones.
2. **Priorizar la estación con mayor tiempo promedio**: una vez cargados los datos, usar el script de análisis para identificar la estación más lenta y revisar si conviene redistribuir tareas, estandarizar el método de trabajo o reducir tiempos muertos entre operaciones.

### Reflexión

- **Más rápido con IA**: redactar el script `analisis.py`, corregir el formato del CSV y preparar el título y la descripción del Pull Request; tareas repetitivas que la IA resolvió en segundos.
- **Cuándo sirvió saber los comandos**: al revisar `git log`, `git branch` y `git pull` pude confirmar que el PR #2 ya estaba fusionado en GitHub y entender exactamente qué cambios trajo el remoto a mi `main` local.
