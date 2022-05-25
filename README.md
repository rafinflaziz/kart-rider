# Introduction
## Game mechanism

KartRider Rush+ is a mobile game developed by Nexon where players can compete and race each other. There are two main mode in the game: Speed race and Item race. Also there are solo mode and team mode. In this project, we will only talk about **team mode**, which is a team consists of 4 players.

**Speed race vs Item race**

In **speed race**, skill is all you need to win. There's no luck involved, so you can win even with a cheap kart if you're skilled enough.
Whether in **item race**, there's some luck involved, and your kart plays important role. There's a huge difference when you use one kart and another, because each kart has unique abilities.

**Average players vs Top players**

In the game, there is a noticeable difference between average players and top players: **win rate (%)**.
Top players are those people who have >75% win rate. They only lose to another top players and extremely lucky opponent.

## Problem

Knowing the game mechanism, I raise a question: **If both use the same karts and builds, what's the difference between average players and top players?**

Both use same kart, both have same luck. But how can top players win so easily? There maybe several aspect that's important in the game, such as: reflex speed, item management, communication, etc.

But I realize something. When I play against top players, they tend to move faster than my team. They always stay at the top position, and they catch up quickly once they fall behind. Therefore, I have one hypothesis about what's the most important thing that differs average players and top players: **Position**.

## What I will do
In this project, I will analyze whether there's a significant difference in position between average players and top players.

# Get the Data
How to get the position?
