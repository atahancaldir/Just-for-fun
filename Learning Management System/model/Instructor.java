package model;

import java.util.ArrayList;
import java.util.Random;

public final class Instructor extends Person {
    private ArrayList<Course> courses = new ArrayList<Course>();

    public Instructor(String name){
        super(name);
        this.initEmail();
    }

    public void addCourse(Course course){
        courses.add(course);
    }

    public void initEmail() {
        String[] splittedName = this.getName().split(" ");

        this.setEmail(splittedName[0].toLowerCase() + "." + splittedName[1].toLowerCase() + "@ozyegin.edu.tr");
    }

    public ArrayList<Course> getCourses(){
        return this.courses;
    }

    public void registerExamGrades(String courseId, String examId, ArrayList<Integer> gradeList){
        for(Course course: courses){
            if(course.getId().equals(courseId)){
                for(int i=0; i<gradeList.size(); i++){
                    course.getStudents().get(i).addGrade(new GradeItem(courseId, examId, gradeList.get(i)));
                }
                return;
            }
        }

        System.out.println("model.Instructor " + this.getName() + " cannot grade the course " + courseId);
    }

    public ArrayList<Integer> listGradesForExam(String courseId, String examId){
        ArrayList<Integer> grades = new ArrayList<Integer>();

        for(Course course: courses){
            if(course.getId().equals(courseId)){
                for(Student student: course.getStudents()){
                    if(student.getGradeItem(courseId, examId) != null){
                        grades.add(student.getGradeItem(courseId, examId).getGrade());
                    }
                }
            }
        }

        return grades;

    }
}
