import pygame
import random
import time

# making screen
pygame.init()

display_width = 1200
display_height = 900

# initiating blank variables

player_value = 0
dealer_value = 0

dealer_one = None
dealer_one_rect = None

dealer_two = None
dealer_two_rect = None

dealer_three = None
dealer_three_rect = None

dealer_four = None
dealer_four_rect = None

dealer_five = None
dealer_five_rect = None

dealer_six = None
dealer_six_rect = None

player_card_one = None
player_card_one_rect = None

player_card_two = None
player_card_two_rect = None

player_card_three = None
player_card_three_rect = None

player_card_four = None
player_card_four_rect = None

player_card_five = None
player_card_five_rect = None

player_card_six = None
player_card_six_rect = None

player_card_seven = None
player_card_seven_rect = None


green = (34, 139, 34)

# starting booleans
going = True
restart = True
show_dealer_one = False
show_dealer_two = False
show_player_one = False
show_player_two = False
show_dealer_three = False
show_dealer_four = False
show_dealer_five = False
show_dealer_six = False
has_not_dealt = True
has_not_stood = True
has_busted = False
show_win = False
show_lose = False
show_push = False

player_card_count = 0

# 52 cards in array
deck = ['c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09', 'c10', 'c11', 'c12', 'c13',
        'd01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd07', 'd08', 'd09', 'd10', 'd11', 'd12', 'd13',
        'h01', 'h02', 'h03', 'h04', 'h05', 'h06', 'h07', 'h08', 'h09', 'h10', 'h11', 'h12', 'h13',
        's01', 's02', 's03', 's04', 's05', 's06', 's07', 's08', 's09', 's10', 's11', 's12', 's13']

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('BlackJack')

# quit button parameter
font = pygame.font.SysFont('Georgia', 40, bold=True)
quit_button_h = 110
quit_button_w = 60
quit_surf = font.render('Quit', True, 'white')
quit_button = pygame.Rect(1090, 0, 110, 60)

# deal button parameters
deal_button_w = 110
deal_button_h = 60
deal_surf = font.render('Deal', True, 'white')
deal_button = pygame.Rect(100, 400, deal_button_w, deal_button_h)

# hit button parameters
hit_button_w = 80
hit_button_h = 60
hit_surf = font.render('Hit', True, 'white')
hit_button = pygame.Rect(100, 500, hit_button_w, hit_button_h)

# stand button
stand_button_w = 140
stand_button_h = 60
stand_surf = font.render('Stand', True, 'white')
stand_button = pygame.Rect(100, 300, stand_button_w, stand_button_h)

# restart button
restart_button_w = 170
restart_button_h = 60
restart_surf = font.render('Restart', True, 'white')
restart_button = pygame.Rect(100, 100, restart_button_w, restart_button_h)

# size of cards
card_original_width = 768
card_original_height = 1063
card_size = ((card_original_width * .2), (card_original_height * .2))

# making card that isn't shown from dealer
card_back = pygame.image.load('Backs/Card-Back-06.png').convert()
card_back_img = pygame.transform.scale(card_back, card_size)
card_back_img_rect = card_back_img.get_rect()
card_back_img_rect.center = (650, 150)

# if the person bust

busted_surf = font.render('You Busted', True, 'blue')
busted_rect = busted_surf.get_rect()
busted_rect.center = (600, 450)

# if the person won
win_surf = font.render('You Won!', True, 'blue')
win_rect = busted_surf.get_rect()
win_rect.center = (600, 450)

# if the person lost
lose_surf = font.render('You Lost.', True, 'blue')
lose_rect = busted_surf.get_rect()
lose_rect.center = (600, 450)

# if the person pushed
push_surf = font.render('You Pushed.', True, 'blue')
push_rect = busted_surf.get_rect()
push_rect.center = (600, 450)


# when cursor goes over button it changes color
def hover(button, surf, width, height):
    if button.x <= a <= button.x + width and button.y <= b <= button.y + height:
        pygame.draw.rect(display, (180, 180, 180), button)
    else:
        pygame.draw.rect(display, (110, 110, 110), button)
    display.blit(surf, (button.x + 5, button.y + 5))


# randomly picks card from array and removes card
def deal(card):
    deck.remove(card)
    card_img = pygame.image.load('Modern/' + card + '.png').convert()
    card_img = pygame.transform.scale(card_img, card_size)

    return card_img


# keeps value of the player
def get_value(val):
    value = int(pick[1:3])
    if val <= 10:
        if value == 1:
            val += 11
    else:
        if value == 1:
            val += 1
    if value >= 10:
        val += 10
    if 1 < value < 10:
        val += value

    return val


pygame.display.update()
# idk some sort of loop - just finsih this part and be done wiht it all
while going:
    display.fill(green)
    if restart:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.collidepoint(events.pos):
                    pygame.quit()

                # deal button only exist once and then disappears
                if has_not_dealt:
                    if deal_button.collidepoint(events.pos):
                        pick = random.choice(deck)
                        dealer_one = deal(pick)
                        dealer_value = get_value(dealer_value)

                        pick = random.choice(deck)
                        dealer_two = deal(pick)
                        dealer_value = get_value(dealer_value)

                        dealer_one_rect = dealer_one.get_rect()
                        dealer_one_rect.center = (550, 150)
                        dealer_two_rect = dealer_two.get_rect()
                        dealer_two_rect.center = (650, 150)
                        show_dealer_one = True
                        has_not_dealt = False

                        # deals the two cards for the player
                        show_player_one = True
                        pick = random.choice(deck)
                        player_card_one = deal(pick)
                        player_card_one_rect = player_card_one.get_rect()
                        player_card_one_rect.center = (550, 600)
                        player_value = get_value(player_value)

                        show_player_two = True
                        pick = random.choice(deck)
                        player_card_two = deal(pick)
                        player_card_two_rect = player_card_two.get_rect()
                        player_card_two_rect.center = (650, 600)
                        player_value = get_value(player_value)

                        player_card_count = 2

                # making hit button only exist if cards have been dealt
                if not has_not_dealt:
                    if has_not_stood:
                        if stand_button.collidepoint(events.pos):
                            has_not_stood = False
                            show_dealer_two = True
                            if dealer_value < 17:
                                pick = random.choice(deck)
                                dealer_three = deal(pick)
                                dealer_value = get_value(dealer_value)
                                dealer_three_rect = dealer_three.get_rect()
                                dealer_three_rect.center = (750, 150)
                                show_dealer_three = True
                                if dealer_value < 17:
                                    pick = random.choice(deck)
                                    dealer_four = deal(pick)
                                    dealer_value = get_value(dealer_value)
                                    dealer_four_rect = dealer_four.get_rect()
                                    dealer_four_rect.center = (850, 150)
                                    show_dealer_four = True
                                    if dealer_value < 17:
                                        pick = random.choice(deck)
                                        dealer_five = deal(pick)
                                        dealer_value = get_value(dealer_value)
                                        dealer_five_rect = dealer_five.get_rect()
                                        dealer_five_rect.center = (950, 150)
                                        show_dealer_five = True
                                        if dealer_value < 17:
                                            pick = random.choice(deck)
                                            dealer_six = deal(pick)
                                            dealer_value = get_value(dealer_value)
                                            dealer_six_rect = dealer_six.get_rect()
                                            dealer_six_rect.center = (1050, 150)
                                            show_dealer_six = True
                            if dealer_value > 21:
                                show_win = True
                            elif dealer_value > player_value:
                                show_lose = True
                            elif dealer_value < player_value:
                                show_win = True
                            elif dealer_value == player_value:
                                show_push = True
                    if has_not_stood and not has_busted:
                        if hit_button.collidepoint(events.pos):
                            player_card_count += 1
                            # just hard coding for cards that at hit 3-7 (come back and be more efficient at this)

                            if player_card_count == 3:
                                pick = random.choice(deck)
                                player_card_three = deal(pick)
                                player_card_three_rect = player_card_three.get_rect()
                                player_card_three_rect.center = (750, 600)
                                player_value = get_value(player_value)
                                if player_value > 21:
                                    show_dealer_two = True
                                    has_busted = True
                            elif player_card_count == 4:
                                pick = random.choice(deck)
                                player_card_four = deal(pick)
                                player_card_four_rect = player_card_four.get_rect()
                                player_card_four_rect.center = (850, 600)
                                player_value = get_value(player_value)
                                if player_value > 21:
                                    show_dealer_two = True
                                    has_busted = True
                            elif player_card_count == 5:
                                pick = random.choice(deck)
                                player_card_five = deal(pick)
                                player_card_five_rect = player_card_five.get_rect()
                                player_card_five_rect.center = (950, 600)
                                player_value = get_value(player_value)
                                if player_value > 21:
                                    show_dealer_two = True
                                    has_busted = True
                            elif player_card_count == 6:
                                pick = random.choice(deck)
                                player_card_six = deal(pick)
                                player_card_six_rect = player_card_six.get_rect()
                                player_card_six_rect.center = (1050, 600)
                                player_value = get_value(player_value)
                                if player_value > 21:
                                    show_dealer_two = True
                                    has_busted = True
                            elif player_card_count == 7:
                                pick = random.choice(deck)
                                player_card_seven = deal(pick)
                                player_card_seven_rect = player_card_seven.get_rect()
                                player_card_seven_rect.center = (1150, 600)
                                player_value = get_value(player_value)
                                if player_value > 21:
                                    show_dealer_two = True
                                    has_busted = True
                if restart_button.collidepoint(events.pos):
                    restart = False
                    time.sleep(1)
                    restart = True

            if show_dealer_one:
                display.blit(dealer_one, dealer_one_rect)
                display.blit(card_back_img, card_back_img_rect)
            if show_dealer_two:
                display.blit(dealer_two, dealer_two_rect)
            if show_dealer_three:
                display.blit(dealer_three, dealer_three_rect)
            if show_dealer_four:
                display.blit(dealer_four, dealer_four_rect)
            if show_dealer_five:
                display.blit(dealer_five, dealer_five_rect)
            if show_dealer_six:
                display.blit(dealer_six, dealer_six_rect)
            if show_player_one:
                display.blit(player_card_one, player_card_one_rect)
            if show_player_two:
                display.blit(player_card_two, player_card_two_rect)
            if player_card_count >= 3:
                display.blit(player_card_three, player_card_three_rect)
            if player_card_count >= 4:
                display.blit(player_card_four, player_card_four_rect)
            if player_card_count >= 5:
                display.blit(player_card_five, player_card_five_rect)
            if player_card_count >= 6:
                display.blit(player_card_six, player_card_six_rect)
            if player_card_count >= 7:
                display.blit(player_card_seven, player_card_seven_rect)
            if has_busted:
                display.blit(busted_surf, busted_rect)
            if show_win:
                display.blit(win_surf, win_rect)
            if show_lose:
                display.blit(lose_surf, lose_rect)
            if show_push:
                display.blit(push_surf, push_rect)
            a, b = pygame.mouse.get_pos()

            # hover color change
            hover(quit_button, quit_surf, quit_button_w, quit_button_h)
            if not has_not_dealt and has_not_stood and not has_busted:
                hover(hit_button, hit_surf, hit_button_w, hit_button_h)
                hover(stand_button, stand_surf, stand_button_w, stand_button_h)

            if has_not_dealt:
                hover(deal_button, deal_surf, deal_button_w, deal_button_h)

            if has_busted or show_win or show_push or show_lose:
                hover(restart_button, restart_surf, restart_button_w, restart_button_h)
            pygame.display.update()

# OVERALL CONCLUSION not bad first project on python
# using logic and classes and OOP stuff needs to be wayyyy better
# this project was not robust at all and all the ifs are just not the way to go
# also effeciency was not good and the restart button does not work so its a one hit wonder
# but it works and we will take it