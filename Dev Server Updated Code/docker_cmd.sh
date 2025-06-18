docker build -t piruby_faculty_processing .
docker run --name piruby_faculty_processing -d -p 8007:8007 piruby_faculty_processing:latest
