from celery import shared_task

from drive.exam.service.ticket_parser import TicketParser


@shared_task
def search_new_tickets():
    parser = TicketParser()
    tickets = parser.find_new_tickets()
    if tickets:
        parser.save_tickets(tickets)
