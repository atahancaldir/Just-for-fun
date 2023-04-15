package gui;

import model.Course;
import model.Instructor;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class JSaveGrades implements ActionListener {
    private Course course;
    private Instructor instructor;
    private JTextField textField;
    private ArrayList<JTextField> grades;
    private JButton refresher;

    public JSaveGrades(Course course, Instructor instructor, JTextField textField, ArrayList<JTextField> grades, JButton refresher){
        this.course = course;
        this.instructor = instructor;
        this.textField = textField;
        this.grades = grades;
        this.refresher = refresher;
    }

    private ArrayList<Integer> getGrades(ArrayList<JTextField> grades){
        ArrayList<Integer> intGrades = new ArrayList<Integer>();

        for(JTextField grade: grades){
            intGrades.add(Integer.parseInt(grade.getText()));
        }

        return intGrades;
    }

    public void actionPerformed(ActionEvent e) {
        if(this.textField.getText().equals("")){
            JOptionPane.showMessageDialog(null, "Enter an exam ID");
            return;
        }

        for(String examID: course.getStudents().get(0).listExamID(course.getId())){
            if(examID.equals(this.textField.getText())){
                JOptionPane.showMessageDialog(null, examID + "'s grades are already entered!");
                return;
            }
        }

        for(JTextField grade: grades){
            if(grade.getText().equals("")){
                JOptionPane.showMessageDialog(null, "Enter all grades!");
                return;
            }
            try {
                if (Integer.parseInt(grade.getText()) < 0 || Integer.parseInt(grade.getText()) > 100) {
                    JOptionPane.showMessageDialog(null, "Enter a valid grade!");
                    return;
                }
            } catch (NumberFormatException exception){
                JOptionPane.showMessageDialog(null, "Enter just numbers!!!");
                return;
            }
        }

        instructor.registerExamGrades(course.getId(), textField.getText(), getGrades(grades));
        this.refresher.doClick();
        JOptionPane.showMessageDialog(null, "Exam grades of " + course.getId() + " are entered successfully!");

    }
}
