# Post 18-O. Registro desde Twitter.

![videos](https://miro.medium.com/max/2000/1*NHi3Nn3Ne5av8CbPQQAVUw.png)

> Nota: todo lo expresado aquí es opinión personal. Suelo escribir sobre mi empresa y nuestro desarrollo tecnológico, sin embargo, en ciertos momentos hay que hablar de lo que hay que hablar.

## La motivación
Quisiera compartir el trabajo personal que realicé la primera semana luego del 18 de Octubre del 2019, día histórico reconocido como el día que ‘Chile despertó’ ([Ver nota en The New York Times](https://www.nytimes.com/2019/11/03/world/americas/chile-protests.html)).

Sin querer tratar de responder las preguntas de fondo de este despertar, lo que se puede decir sin temor a dudas, es que representa en muchos aspectos una de las principales demostraciones sociales de reclamo contra lo ético del modelo económico liberal. Consideración que comparto, en tanto que si no ponemos en el centro los valores más que la norma sobre la cual construímos riqueza, estaremos dejando de lado al 99% de la población mundial fuera del beneficio de dicha riqueza. Y lo digo siendo el fundador de una Startup que juega todos los días con las reglas del juego liberal. Al respecto del dilema ético del Capitalismo, recomiendo leer a Paul Collier ([Ver aquí](https://www.amazon.com/Future-Capitalism-Facing-New-Anxieties/dp/0062748653)).

El impulso de comprender que lo que pasó (y pasa) en Chile, es un síntoma de un fenómeno global en el cual la Democracia y el Liberalismo chocan, quise registrar qué sucedía en los días siguientes al [18 de Octubre](https://redgol.cl/tendencias/A-un-ano-del-estallido-social-Que-paso-el-18-de-octubre-en-Chile-cronologia-de-lo-sucedido-en-Chile-20201016-0085.html), día en el cuál ocurrieron hechos graves como la quema del Metro por ejemplo (que aún sigue sin culpables).

Debo adelantar que el registro no es bonito.

## El método
Twitter se vuelve una interesante fuente de datos producidos en tiempo real. Ya es sabido que podemos usar su API para extraer texto, sin embargo también podemos obtener media, como imágenes o video.

Lo que quise hacer en este caso, fue acceder a los videos que los usuarios producían al momento que los hechos se iban registrando. Para esto, hice un script sencillo de Python, que filtrara cuando el contenido era video.

Junto con esto, y para tener los videos relevantes, agregué otro filtro. En este caso, lo que hice fue decirle a Twitter que buscara en hasthtags específicos, los cuáles supuse cambiarían a medida que pasaban las horas. Es así que cada vez que hacía una llamada a la API, consultaba (web crawling) en el sitio [Trends24/Chile](https://trends24.in/chile/), qué era lo más tweeteado. El resultado de esta parte es un archivo CSV con el nombre de usuario(a), url del video, fecha en la que fue producido, y el hashtag mediante el cual fue encontrado ese contenido.

Luego de esto lo que hice fue descartar duplicados de un total de más de 22 mil url’s a videos y descargar aquellos posiblemente únicos. Digo posiblemente porque obtuve más de 2.600 videos deduplicados. Manualmente reduje esa cifra a poco más de 1.200, eliminando además videos que no tenían relación y fueron entregados por la API de Twitter. Mucho video de los Simpsons (ja!). El código para la descarga de los videos, [aquí](https://github.com/crishernandezmaps/18O).

> El código completo se puede clonar o descargar aquí: https://github.com/crishernandezmaps/18O

El resultado, el pull de videos con los que me quedé no son nada de lindos. Muestran abusos, violencia innecesaria y desesperanza. Sin embargo, todo esto es humano y vale la pena tener registro para que no siga ocurriendo.

La selección de videos, como explique más adelante no tiene una ‘línea ediorial’, hay videos de celulares como captura de pantalla o grabando la pantalla de la televisión. Lo que me importó es que fuese lo que la ciudadanía quería compartir. Tampoco tiene mi sesgo político (al menos explícito), como un factor en la edición.

## El resultado

Hay imágenes fuertes en los videos, por eso no inserto algunos de muestra aquí, pero dejo uno que fue el resultado de esa semana: ‘La Marcha más grande de Chile’ ([saber más](https://www.bbc.com/mundo/noticias-america-latina-50190029)):

![marcha](https://youtu.be/blHqHBqJALI)

Finalmente, aquí se pueden encontrar TODOS los videos: https://mega.nz/folder/M1NW2JwC#F-vCtyhmRjvoDJ-hO-3ceg

