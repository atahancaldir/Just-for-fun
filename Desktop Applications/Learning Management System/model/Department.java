package model;

import java.util.ArrayList;

public final class Department {
    private String name;
    private ArrayList<Course> courses = new ArrayList<Course>();
    private ArrayList<Instructor> instructors = new ArrayList<Instructor>();
    private ArrayList<Student> students = new ArrayList<Student>();

    public Department(String name){
        this.name = name;
    }

    public void addInstructor(String instructorName){
        instructors.add(new Instructor(instructorName));
    }

    public void addStudent(String studentName){
        students.add(new Student(studentName));
    }

    public void assignInstructorToCourse(String instructorName, String courseId){
        if(this.getInstructorByName(instructorName) == null){
            return;
        }

        if(this.getCourse(courseId) == null){
            return;
        }

        for(Course course: courses){
            if(course.getId().equals(courseId)){
                for(Instructor instructor: instructors){
                    if(instructor.getName().equals(instructorName)){
                        course.setInstructor(instructor);
                        instructor.addCourse(course);
                    }
                }
            }
        }
    }

    public void createCourse(String courseId, String courseName){
        courses.add(new Course(courseId, courseName));
    }

    public ArrayList<Instructor> getInstructors() {
        return instructors;
    }

    public Course getCourse(String st) {
        for(Course course: courses){
            if(course.getId().equals(st) || course.getName().equals(st)){
                return course;
            }
        }

        System.out.println("model.Course not found: " + st);
        return null;
    }

    public ArrayList<Student> getStudents() {
        return students;
    }

    public Instructor getInstructorByName(String instructorName){
        for(Instructor instructor: instructors){
            if(instructor.getName().equals(instructorName)){
                return instructor;
            }
        }

        System.out.println("model.Instructor not found: " + instructorName);
        return null;
    }

    public void listInstructors(){
        if(instructors.size() == 0){
            System.out.println("No instructor found");
            return;
        }

        System.out.println("Instructors registered in this department are:");

        for(Instructor instructor: instructors){
            System.out.println(instructor.getId() + ", " + instructor.getName() + ", " + instructor.getEmail());
        }
    }

}
