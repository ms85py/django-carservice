
from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        cont = [
            {'type': 'Change Oil', 'link': '/get_ticket/change_oil'},
            {'type': 'Inflate tires', 'link': '/get_ticket/inflate_tires'},
            {'type': 'Get diagnostic test', 'link': '/get_ticket/diagnostic'}
                ]
        context_final = {'ctx': cont}
        return render(request, 'tickets/menu.html', context=context_final)


class TicketView(View):
    ticket_nr = 0
    tickets = {
        "oil": [],
        "tires": [],
        "diagnostic": [],
    }
    processed = []

    def calc(self, to_do):
        time = len(TicketView.tickets['oil']) * 2
        if to_do == "oil":
            return time
        time += len(TicketView.tickets['tires']) * 5
        if to_do == "tires":
            return time
        time += len(TicketView.tickets['diagnostic']) * 30
        return time

    def get(self, request, link, *args, **kwargs):
        if "_" in link:
            link = link.split('_')[1]
        else:
            link = link
        TicketView.ticket_nr += 1
        wait = self.calc(link)
        TicketView.tickets[link].append(TicketView.ticket_nr)
        context = {"ticket_nr": TicketView.ticket_nr, "wait_time": wait}
        return render(request, 'tickets/ticket.html', context=context)


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        cont = [
            {'type': 'Change oil queue', 'que': len(TicketView.tickets['oil'])},
            {'type': 'Inflate tires queue', 'que': len(TicketView.tickets['tires'])},
            {'type': 'Get diagnostic queue', 'que': len(TicketView.tickets['diagnostic'])},
                ]
        context = {'ctx': cont}
        return render(request, 'tickets/process.html', context=context)


    def post(self, request, *args, **kwargs):

        if TicketView.tickets['oil']:
            TicketView.processed.append(TicketView.tickets['oil'].pop(0))
        elif TicketView.tickets['tires']:
            TicketView.processed.append(TicketView.tickets['tires'].pop(0))
        elif TicketView.tickets['diagnostic']:
            TicketView.processed.append(TicketView.tickets['diagnostic'].pop(0))

        return redirect('/next')


class NextTicketView(View):
    def get(self, request, *args, **kwargs):

        if TicketView.processed:
            ticket = f"Next ticket #{TicketView.processed[-1]}"
        else:
            ticket = f"Waiting for the next client"

        cont = {'ticket': ticket}
        context = {'ctx': cont}
        return render(request, 'tickets/next_ticket.html', context=context)

