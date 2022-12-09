from django.db import models



class Technique_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class Engine_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

class Transmission_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class Drive_axle_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class Steerable_axle_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class Car(models.Model):
    factory_number = models.TextField(max_length=17, unique=True, verbose_name='Заводской номер')
    technique_model = models.ForeignKey(Technique_model, on_delete=models.CASCADE)
    engine_model = models.ForeignKey(Engine_model, on_delete=models.CASCADE)
    engine_number = models.TextField(max_length=17, verbose_name='Номер двигателя')
    transmission_model = Engine_model = models.ForeignKey(Engine_model, on_delete=models.CASCADE)
    transmission_number = models.TextField(max_length=50, verbose_name='Номер трансмиссии')
    drive_axle_model = models.ForeignKey(Drive_axle_model, on_delete=models.CASCADE)
    drive_axle_number = models.TextField(max_length=50, verbose_name='Номер ведущего моста')
    steerable_axle_model = models.ForeignKey(Drive_axle_model, on_delete=models.CASCADE)
    steerable_axle_number = models.TextField(max_length=50, verbose_name='Номер управляемого моста')
    supply_contract = models.TextField(max_length=50, verbose_name='Договор поставки №, дата.')
    date_of_shipment_from_the_factory = models.DateTimeField(verbose_name='Дата отгрузки с завода')
    consignee = models.TextField(max_length=50, verbose_name='Грузополучатель')
    delivery_address = models.TextField(max_length=150, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(max_length=150, verbose_name='Комплектация (доп. опции)')
    client = models.TextField(max_length=150, verbose_name='Клиент')
    service_company = models.TextField(max_length=150, verbose_name='Клиент')

