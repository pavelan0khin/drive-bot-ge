# from django.test import TestCase
# from drive.exam.models import Ticket
#
#
# tickets_ids = [
#     68,
#     146,
#     346,
#     368,
#     421,
#     449,
#     461,
#     500,
#     507,
#     515,
#     571,
#     638,
#     660,
#     777,
#     829,
#     858,
#     921,
#     987,
#     997,
#     1015,
#     1037,
#     1076,
#     1131,
#     1154,
#     1158,
#     1181,
#     1215,
#     1248,
#     1282,
#     1381,
# ]
#
# tickets = Ticket.objects.filter(external_id__in=tickets_ids)
#
#
# data = {}
# for ticket in tickets:
#     data[ticket.external_id] = ticket.topic.name.get("ru")
#
# for key, value in data.items():
#     print(key, value, sep=": ")


from drive.exam import models

tickets = models.Ticket.objects.all()
session = models.Session.objects.get(id=66)
session.tickets.add(*tickets)
session.save()
