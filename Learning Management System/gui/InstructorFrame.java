package gui;

import model.Course;
import model.Department;
import model.Instructor;

import java.awt.*;
import java.awt.event.ActionListener;
import java.util.List;

import javax.swing.*;


public class InstructorFrame extends JFrame {
    private Department department;
    private Instructor instructor;
    public static boolean isOpen = false;

    public InstructorFrame(Instructor instructor, Department department) {
        this.instructor = instructor;
        this.department = department;
        this.isOpen = true;
        init();
    }

    private void init() {
        this.setSize(800, 600);
        this.setLocationRelativeTo(null);

        this.addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent windowEvent) {
                isOpen = false;
            }
        });

        JTabbedPane tabbedPane = new JTabbedPane();

        for(Course course: this.instructor.getCourses()){
            JPanel panel = new JPanel(new BorderLayout());
            tabbedPane.addTab(course.getId(), panel);

            JPanel topPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
            topPanel.setBackground(new Color(51, 85, 144));
            panel.add(topPanel, BorderLayout.NORTH);

            JPanel mainPanel = new JPanel();
            mainPanel.setBackground(new Color(94, 133, 197));
            panel.add(mainPanel, BorderLayout.CENTER);

            JButton listStudents = new JButton("List Students");
            JButton registerExam = new JButton("Register Exam Grades");
            JButton listGrades = new JButton("List Grades");

            JListStudents listStudentsListener = new JListStudents(mainPanel, course);
            listStudents.addActionListener(listStudentsListener);

            JRegisterGrades registerGradesListener = new JRegisterGrades(mainPanel, course, instructor, registerExam);
            registerExam.addActionListener(registerGradesListener);

            JListGrades listGradesListener = new JListGrades(mainPanel, course);
            listGrades.addActionListener(listGradesListener);

            topPanel.add(listStudents);
            topPanel.add(registerExam);
            topPanel.add(listGrades);
        }

        this.add(tabbedPane);

        this.setVisible(true);

    }

}
