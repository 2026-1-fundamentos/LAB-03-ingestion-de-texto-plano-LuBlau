"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

    with open(
        "files/input/clusters_report.txt",
        "r",
        encoding="utf-8",
    ) as archivo:
        lineas = archivo.readlines()

    datos = []

    i = 4
    while i < len(lineas):

        if re.match(r"\s*\d+\s", lineas[i]):

            patron = re.match(
                r"\s*(\d+)\s+(\d+)\s+([\d,]+)\s+%\s+(.*)",
                lineas[i],
            )

            cluster = int(patron.group(1))
            cantidad = int(patron.group(2))
            porcentaje = float(patron.group(3).replace(",", "."))
            palabras = patron.group(4).strip()

            i += 1

            while (
                i < len(lineas)
                and lineas[i].strip() != ""
                and not re.match(r"\s*\d+\s", lineas[i])
            ):
                palabras += " " + lineas[i].strip()
                i += 1

            palabras = palabras.rstrip(".")
            palabras = re.sub(r"\s+", " ", palabras)
            palabras = re.sub(r"\s*,\s*", ", ", palabras)

            datos.append(
                [
                    cluster,
                    cantidad,
                    porcentaje,
                    palabras,
                ]
            )

        else:
            i += 1

    return pd.DataFrame(
        datos,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )