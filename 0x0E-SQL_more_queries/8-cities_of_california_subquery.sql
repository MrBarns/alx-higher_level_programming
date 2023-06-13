-- Display cities in California
-- Select cities of Carlifornia in database
SELECT * FROM cities
WHERE state_id = (
  SELECT id FROM states
  WHERE `name` = "California"
  )
ORDER BY id ASC;
