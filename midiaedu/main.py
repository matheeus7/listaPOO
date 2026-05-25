from models.plataformass import Plataformas
from models.cast import Podcast
from models.textonarrado import TextoNarrado
from models.video import Video

video = Video("Barcelona Vs Bayern", "120", "1440p")
text = TextoNarrado("Livro genesis", "120", "Portugues Brasil")
pod = Podcast("Podcast sobre futebol", "60" , "João Silva")

plata = Plataformas("Playlist insana")


plata.adicionar_midia(video)
plata.adicionar_midia(text)
plata.adicionar_midia(pod)

plata.listar_midias()

plata.reproduzir_todas_midias()