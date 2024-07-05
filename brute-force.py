def brute_force(text, pattern):
    l1 = len(text)  # Longitud del texto
    l2 = len(pattern)  # Longitud del patrón

    i = 0  # Variable para el bucle del texto

    flag = False  # Bandera para verificar si el patrón está presente en el texto

    while i < l1:  # Iterar desde el índice 0 del texto hasta len-1 de texto

        j = 0  # Variable para el bucle del patrón
        count = 0  # Variable para contar cuántos caracteres coinciden

        while j < l2:  # Iterar desde el índice 0 del patrón hasta len-1 de patrón
            # Si el índice actual más el índice del patrón es menor que la longitud del texto y el carácter actual del texto es igual al carácter actual del patrón
            if i + j < l1 and text[i + j] == pattern[j]:
                count += 1  # Incrementar el contador si los caracteres coinciden
            else:
                break

            j += 1  # Incrementar el índice del patrón para comparar el siguiente carácter

        if count == l2:  # Si el contador es igual a la longitud del patrón
            print("\nPattern occurs at index", i)
            flag = True  # Establecer la bandera en True

        i += 1  # Incrementar el índice del texto para comparar el siguiente carácter

    # Si la bandera es False, imprimir que el patrón no está presente en el texto
    if not flag:
        print("\nPattern is not all present in the text")


brute_force('Hola mundo', 'mundo')
brute_force('ababababcbbababab', 'abc')

# "Shift" desplazamiento de un lugar.
