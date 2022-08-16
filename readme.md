# Hava Durumu Uygulaması
Django ile İl , İlçe, Hava durumu modelleri ve redis, docker teknolojileri kullanılarak bir uygulama hazırlanmıştır.  

## Hazırlayan
* Özgür Durak

## Kurulum
Proje için docker teknolojisi kullanılmıştır. Bundan dolayı aşağıda belirtilen komutun projenin ana dizininde çalıştırılması sonucu websitesi çalışır hale gelecektir.
Komutu kullanmadan önce ``.env.example`` dosyası kopyalanarak ``.env`` dosyası oluşturulmalı ve içeriğinde gerekli alanlar doldurulmalıdır.
```
docker-compose up --build
```

## Gereksinimler

```
asgiref==3.5.2  
async-timeout==4.0.2  
certifi==2022.6.15  
charset-normalizer==2.1.0  
Deprecated==1.2.13  
Django==4.1  
djangorestframework==3.13.1  
hiredis==2.0.0  
idna==3.3  
packaging==21.3  
pip==22.2.1  
psycopg2-binary==2.9.3  
pyparsing==3.0.9  
pytz==2022.1  
redis==4.3.4  
requests==2.28.1  
setuptools==63.2.0  
sqlparse==0.4.2  
urllib3==1.26.11  
wrapt==1.14.1
```
## Uygulama URL Yapısı

* ``/provience`` - İl için CRUD aksiyonlarını içeren endpoint.
* ``/town`` - İl.e için CRUD aksiyonlarını içeren endpoint.
* ``/weather`` - Hava Durumu Uygulaması UI Base Dizin
* ``/weather/provience`` - Hava Durumu Uygulaması İl Seçim Sayfası
* ``/weather/provience/{provinceId}`` - Hava Durumu Uygulaması İl ve altındaki ilçeler için hava durumu rapor sayfası