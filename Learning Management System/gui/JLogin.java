package gui;

import model.Department;
import model.Instructor;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class JLogin implements ActionListener {
    private JTextField textField;
    private Department department;
    private Instructor instructor;

    public JLogin(JTextField textField, Department department){
        this.textField = textField;
        this.department = department;
    }

    public void actionPerformed(ActionEvent e) {
        String email = textField.getText();
        instructor = null;

        if(!email.endsWith("@ozyegin.edu.tr")){
            JOptionPane.showMessageDialog(null, "invalid e-mail address!");
            return;
        }

        for(Instructor instructor: department.getInstructors()){
            if(instructor.getEmail().equals(email)){
                this.instructor = instructor;
            }
        }

        if(this.instructor == null){
            JOptionPane.showMessageDialog(null, "Instructor not found!");
            return;
        }


        if(this.instructor.getCourses().size() == 0){
            JOptionPane.showMessageDialog(null, "Instructor has no courses");
            return;
        }

        if(InstructorFrame.isOpen == true){
            JOptionPane.showMessageDialog(null, "Only one enterance is allowed!");
            return;
        }

        new InstructorFrame(this.instructor, department);
    }
}
