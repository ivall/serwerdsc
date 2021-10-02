Prosty projekt umożoiwiający tworzenie właścicielom serwerów discord własnych stron dla ich serwerów.
#### Endpointy
| Metoda        | Endpoint      |  Akcja  |
| ------------- | ------------- | -------------
| GET  | /api/servers/  |  Zwraca wszystkie serwery dodane do bazy
| GET  | /api/servers/:discord_id/ | Zwraca serwer, którego pole discord_id odpowiada podanemu w URL
| POST | /api/servers/ | Tworzy nowy serwer. Jeżeli w bazie jest już jakiś serwer z takim samym discord_id aktualizuje jego dane o te podane

API wymaga używania tokenu, który ustawiamy w pliku config.py.
