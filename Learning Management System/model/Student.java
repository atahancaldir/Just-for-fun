package model;

import java.util.ArrayList;

public final class Student extends Person{
    private ArrayList<Course> enrolledCourses = new ArrayList<Course>();
    private ArrayList<GradeItem> grades = new ArrayList<GradeItem>();

    public Student(String name){
        super(name);
        this.initEmail();
    }

    public void initEmail() {
        String[] splittedName = this.getName().split(" ");

        this.setEmail(splittedName[0].toLowerCase() + "." + splittedName[1].toLowerCase() + "@ozu.edu.tr");
    }

    public void registerToCourse(Course course){
        if(course.getInstructor() == null){
            System.out.println("model.Course not available");
            return;
        }

        enrolledCourses.add(course);
        course.addStudent(this);
    }

    public void dropCourse(Course course){
        if(course.getInstructor() == null){
            return;
        }

        enrolledCourses.remove(course);
        course.removeStudent(this);
    }

    public void addGrade(GradeItem gradeitem){
        grades.add(gradeitem);
    }

    public GradeItem getGradeItem(String courseId, String examId){
        for(GradeItem grade: grades){
            if(grade.getCourseId().equals(courseId) && grade.getExamId().equals(examId)){
                return grade;
            }
        }

        System.out.println("No Grade Item found");
        return null;
    }

    public ArrayList<String> listExamID(String courseId){
        ArrayList<String> examIDs = new ArrayList<String>();

        for(Course course: enrolledCourses) {
            if (course.getId().equals(courseId)) {
                for (GradeItem grade : grades) {
                    if (grade.getCourseId().equals(course.getId())) {
                        examIDs.add(grade.getExamId());
                    }
                }
            }
        }

        return examIDs;
    }

}
