import streamlit as st
import random


#1.

st.title("Bienvenido")

nombre = st.text_input("Escribe tu nombre:")

if nombre:
    st.write(f"¡Hola, {nombre}!")

    st.divider()

#2.


n1 = st.number_input("Ingresa el primer número:", key="n1_ej2")
n2 = st.number_input("Ingresa el segundo número:", key="n2_ej2")

producto = n1 * n2
st.write(f"El resultado de la multiplicación es: **{producto}**")

if n1 > 100 or n2 > 100:
    st.warning("Números grandes")

    st.divider()

#3.

st.subheader("Ejercicio 3: Convertidor de Temperatura")
opcion = st.radio(
    "Selecciona la conversión:",
    ("Celsius a Fahrenheit", "Fahrenheit a Celsius"),
    key="radio_ej3"
)
temp = st.number_input("Ingresa la temperatura:", key="temp_ej3")

if "Celsius" in opcion:
    resultado = (temp * 9/5) + 32
    st.success(f"{temp}°C equivale a {resultado:.2f}°F")
else:
    resultado = (temp - 32) * 5/9
    st.success(f"{temp}°F equivale a {resultado:.2f}°C")

st.divider()

#4.

st.subheader("Ejercicio 4: Galería de Mascotas")
tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.image("https://placekitten.com/400/300", caption="Un gatito tierno")
    if st.button("Me gusta el gato", key="like_gato"):
        st.toast("Te gusta esta mascota")

with tab2:
    st.image("https://placedog.net/400/300", caption="Un perro fiel")
    if st.button("Me gusta el perro", key="like_perro"):
        st.toast("Te gusta esta mascota")

with tab3:
    st.image("https://picsum.photos/id/237/400/300", caption="Un ave colorida")
    if st.button("Me gusta el ave", key="like_ave"):
        st.toast("Te gusta esta mascota")

        st.divider()

        #5.

        st.subheader("Ejercicio 5: Caja de Comentarios")
with st.form("mi_formulario"):
    asunto = st.text_input("Asunto:")
    mensaje = st.text_area("Mensaje:")
    enviado = st.form_submit_button("Enviar")

if enviado:
    if mensaje.strip():
        st.json({"Asunto": asunto, "Mensaje": mensaje})
    else:
        st.error("El mensaje no puede estar vacío.")

st.divider()

#6.
# st.subheader("Ejercicio 6: Login Simulado")


if "logeado" not in st.session_state:
    st.session_state.logeado = False

if not st.session_state.logeado:
    user = st.text_input("Usuario:", key="user_login")
    pw = st.text_input("Contraseña:", type="password", key="pw_login")
    if st.button("Ingresar", key="btn_login"):
        if user == "admin" and pw == "1234":
            st.session_state.logeado = True
            st.rerun() 
        else:
            st.error("Credenciales incorrectas")
else:
    st.success("¡Bienvenido, administrador!")
    if st.button("Cerrar Sesión", key="logout"):
        st.session_state.logeado = False
        st.rerun()

st.divider()

#7.

st.subheader("Ejercicio 7: Lista de Compras")

if "lista_compras" not in st.session_state:
    st.session_state.lista_compras = []

producto_nuevo = st.text_input("Producto a agregar:", key="input_compra")

col1, col2 = st.columns(2)
with col1:
    if st.button("Agregar", key="add_item"):
        if producto_nuevo:
            st.session_state.lista_compras.append(producto_nuevo)
with col2:
    if st.button("Limpiar Lista", key="clear_list"):
        st.session_state.lista_compras = []

st.write("### Tu lista:")
for item in st.session_state.lista_compras:
    st.write(f"- {item}")

st.divider()

### Ejercicio 8: Gráfico Interactivo
st.subheader("Ejercicio 8: Gráfico Interactivo")
n_aleatorios = st.slider("Selecciona N:", 10, 100, 50, key="slider_ej8")

datos = [random.randint(0, 100) for _ in range(n_aleatorios)]
st.line_chart(datos)

if st.button("Regenerar datos", key="regen_ej8"):
    st.rerun()