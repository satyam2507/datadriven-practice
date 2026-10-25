select pipe_name, min(start_at) as first_run,max(start_at) as last_run,count(distinct(substring(start_at,1,7))) as active_months 
from data_pipes 
group by pipe_name;
