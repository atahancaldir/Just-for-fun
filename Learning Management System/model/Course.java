package model;

import java.util.ArrayList;

public final class Course {
    private String id;
    private String name;
    private Instructor instructor;
    private ArrayList<Student> students = new ArrayList<Student>();

    public Course(String courseId, String courseName){
        this.id = courseId;
        this.name = courseName;
    }

    public void addStudent(Student student){
        if(instructor == null){
            System.out.println("model.Course not available");
            return;
        }
        
        if(students.contains(student)){
            System.out.println("model.Student is already in this course");
            return;
        }

        students.add(student);
    }

    public void removeStudent(Student student){
        if(instructor == null){
            System.out.println("model.Course not available");
            return;
        }

        if(!students.contains(student)){
            System.out.println("model.Student does not in this course");
            return;
        }

        students.remove(student);
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Instructor getInstructor() {
        if(instructor == null){
            return null;
        }

        return instructor;
    }

    public ArrayList<Student> getStudents() {
        return students;
    }

    public void setInstructor(Instructor instructor) {
        this.instructor = instructor;
    }

}
