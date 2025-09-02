SELECT movies.title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
where people.name = 'Bradley Cooper' AND movies.title IN(
SELECT movies.title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
where people.name = 'Jennifer Lawrence')
ORDER BY movies.title;
