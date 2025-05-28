def highlight(row):
    if "Realizado" in row['Estado']:
        return ['background-color: darkgreen; color: black' for _ in row]
    elif "En curso" in row['Estado']:
        return ['background-color: darkgoldenrod; color: black' for _ in row]
    elif row['Estado'] == "Vacio":
        return ['background-color: #be1e2d; color: black' for _ in row]
    elif "Arribado" in row['Estado']:
        return ['background-color: darkgreen; color: black' for _ in row]
    elif row['Estado'] == "Pendiente ingreso":
        return ['background-color: darkgoldenrod; color: black' for _ in row]
    else:
        return ['' for _ in row]
