SELECT AVG(energy) FROM songs WHERE artist_id =
    (SELECT ID FROM artists WHERE name = 'Drake');
