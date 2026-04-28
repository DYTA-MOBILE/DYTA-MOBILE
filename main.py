import yt_dlp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

# --- LÓGICA DE BÚSQUEDA (Igual que en tu PC) ---
def buscar_musica(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'extract_flat': True,
        'nocheckcertificate': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Añadimos el filtro para evitar anuncios como pediste
            res = ydl.extract_info(f"ytsearch10:{query} official music video", download=False)
            return [{'text': e.get('title'), 'url': f"https://www.youtube.com/watch?v={e.get('id')}"} 
                    for e in res.get('entries', [])]
        except:
            return []

# --- INTERFAZ DYTA MOBILE ---
class DytaInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 10
        self.spacing = 10

        # Buscador
        self.input = TextInput(hint_text="Buscar en DYTA...", size_hint_y=None, height=120, multiline=False)
        self.add_widget(self.input)

        # Botón Buscar
        btn = Button(text="BUSCAR", size_hint_y=None, height=100, background_color=get_color_from_hex('#bada55'))
        btn.bind(on_press=self.realizar_busqueda)
        self.add_widget(btn)

        # Lista de Resultados
        self.resultados = RecycleView()
        self.add_widget(self.resultados)

    def realizar_busqueda(self, instance):
        query = self.input.text
        if query:
            datos = buscar_musica(query)
            self.resultados.data = datos

class DytaApp(App):
    def build(self):
        return DytaInterface()

if __name__ == '__main__':
    DytaApp().run()