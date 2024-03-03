from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from .models import Player, MatchResult
from django.urls import reverse
import random

def main(request):
    if request.method == 'POST':
        playername = request.POST.get('name')
        if playername.strip() == "":
            messages.warning(request, 'Please enter a valid name.')
            return redirect('main')
        elif MatchResult.objects.filter(player1_name__iexact=playername).exists():
            messages.warning(request, 'This name is already taken, please try another one.')
            return redirect('main')
        else:
            messages.success(request, f'Welcome, {playername}!')
            request.session['playername'] = playername
            return redirect('game')
    return render(request, 'main.html')

def game(request):
    if request.method == 'POST':
        if 'playername' not in request.session:
            # Handle unauthenticated user
            messages.warning(request, 'Please enter your name first.')
            return redirect('main')

        user_move = request.POST.get('move')
        npc_move = random.choice(["rock", "paper", "scissors"])
        winner = select_winner(user_move, npc_move)

        match_result = MatchResult.objects.create(
            player1_name=request.session['playername'],
            player2_name='Bot',  
            player1_move=user_move,
            player2_move=npc_move,
            winner=winner
        )
  
        return redirect('results')
    else:
        return render(request, 'actual_game.html')

def rules(request):  
    return render(request, 'rules.html')

def make_move(request):
    options = ["rock", "paper", "scissors"]
    human_choice = request.GET.get('move')
    
    if human_choice not in options:
        return JsonResponse({'error': 'Invalid move'}, status=400)
    
    npc_choice = random.choice(options)
    winner = select_winner(human_choice, npc_choice)
    return JsonResponse({'winner': winner})

def select_winner(human_choice, npc_choice):
    if human_choice == npc_choice:
        return "We're even Stevens!"
    elif (human_choice == "rock" and npc_choice == "scissors") or \
         (human_choice == "paper" and npc_choice == "rock") or \
         (human_choice == "scissors" and npc_choice == "paper"):
        return "Human is the champ!"
    else:
        return "Npc is the champ!"
    
def end_game(request):
    if 'playername' in request.session:
        del request.session['playername']
    return redirect('main')

def results(request):
    results = MatchResult.objects.all()
    return render(request, 'results.html', {'results': results})
