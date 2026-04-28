import yt_dlp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty

# --- LÓGICA DE BÚSQUEDA ---
def buscar_musica(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'extract_flat': True,
        'nocheckcertificate': True,
        # Filtro para contenido real y no anuncios
        'match_filter': yt_dlp.utils.match_filter_func("!is_live & duration > 60")
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Buscamos con términos específicos para mejores resultados
            res = ydl.extract_info(f"ytsearch10:{query} official music video", download=False)
            return [{'text': e.get('title'), 'url': f"https://www.youtube.com/watch?v={e.get('id')}"} 
                    for e in res.get('entries', []) if e]
        except:
            return []

# --- INTERFAZ DYTA MOBILE ---
class DytaInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        # Números limpios sin ceros delante para evitar el SyntaxError
        self.padding = 10
        self.spacing = 10

        # Buscador: altura ajustada para dedo
        self.input = TextInput(
            hint_text="Buscar en DYTA...", 
            size_hint_y=None, 
            height=120, 
            multiline=False
        )
        self.add_widget(self.input)

        # Botón Buscar
        btn = Button(
            text="BUSCAR MUSICA", 
            size_hint_y=None, 
            height=100, 
            background_color=get_color_from_hex('#bada55'),
            font_size=20
        )
        btn.bind(on_press=self.realizar_busqueda)
        self.add_widget(btn)

        # Lista de Resultados
        self.resultados = RecycleView()
        self.resultados.viewclass = 'Button' # Usamos botones para que sean clicables
        self.add_widget(self.resultados)

    def realizar_busqueda(self, instance):
        query = self.input.text
        if query:
            self.resultados.data = [] # Limpiamos antes de buscar
            datos = buscar_musica(query)
            self.resultados.data = datos

class DytaApp(App):
    def build(self):
        self.title = 'DYTA MUSICA'
        return DytaInterface()

if __name__ == '__main__':
    DytaApp().run()