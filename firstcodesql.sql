create or replace function car_count( mak varchar) 
	returns table (
		car_model varchar,
		car_price numeric
	) 
	language plpgsql
as $$
begin
	return query 
		select
			model,
			price
		from
			car
		where
			car.make=mak;
end;
$$



SELECT * from car_count('Audi');
SELECT * from car_count('Volvo');

#adding comment on github for branch sqlcodecommmentbranch
