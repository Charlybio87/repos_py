#---Comentario de Documentacion---
#CISCO_PYTHON 1
#Programa: "Primeros pasos de Python"
#@author: Ribas Carlos
#@version 1.0.1
#@see: """

#---Comentario de bloque--- (este coment. no se visualiza en documentacion)
# Realizando Seguimiento del Modulo 2 
# Función print()

#---Comentario de Linea---
print("1.¡Hola Mundo!") # Una cadena como el argumento de la función print()

print("2.La Witsi Witsi Araña subió a su telaraña.") # Instrucciones
print("Vino la lluvia y se la llevó.")

print("3.La Witsi Witsi Araña subió a su telaraña.")
print()
print("Vino la lluvia y se la llevó.")


print("4.La Witsi Witsi Araña\nsubió a su telaraña.") #Caracteres de escape(\n) y 
print()                                               #nueva línea en Python
print("Vino la lluvia\ny se la llevó.") 

print("5.La Witsi Witsi Araña subió a su telaraña.")
print() # \m \l \o \p \a no realizan nada.
print("Vino la lluvia y se la llevó.")

print("6.La Witsi Witsi Araña" , "subió" , "a su telaraña.") #Usando múltiples argumentos (x3)

print("7.Mi nombre es", "Python.") #Argumentos posicionales
print("Monty Python.")

print("8.Mi nombre es", "Python.", end="") #Argumentos de palabras clave
print("Monty Python.")                      
print("Mi nombre es ", end="  ")
print("Monty Python.")
print("Mi nombre es ", end="        ") # Se visualiza un espacio mucho mayor 
print("Monty Python.")                 # entre ambos argumentos

print("9.Mi nombre es ", end="\n")  # \n salto de linea
print("Monty Python.")

print("10.Mi", "nombre", "es", "Monty", "Python.", sep="-") #separacion de c/argumento con -

print("11.Mi", "nombre", "es", sep="_", end="*") # Palabra clave pueden mezclarse en una 
print("Monty", "Python.", sep="*", end="*\n")    # invocación. #end=""(fin arg),sep="-"(entre argum)
                                                
print("LAB12. Programming","Essentials","in", sep="***", end="...") #sin \n no hay salto de linea
print("Python")                                                 

print ("LAB13")
###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

print("15.1\nMi\nnombre\nes\nBond.", end=" ")
print("James Bond.")
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
