package gui;

import model.Course;
import model.Instructor;
import model.Student;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class JRegisterGrades implements ActionListener {
    private JPanel panel;
    private Course course;
    private Instructor instructor;
    private JButton refresher;

    public JRegisterGrades(JPanel panel, Course course, Instructor instructor, JButton refresher){
        this.panel = panel;
        this.course = course;
        this.instructor = instructor;
        this.refresher = refresher;
    }

    public void actionPerformed(ActionEvent e) {
        if(course.getStudents().size() == 0){
            JOptionPane.showMessageDialog(null, "There are no students taking this course!");
            return;
        }

        ArrayList<JTextField> grades = new ArrayList<JTextField>();

        panel.removeAll();
        panel.setLayout(new BorderLayout());

        JPanel info = new JPanel(new GridLayout(course.getStudents().size()+2, 3, 0, 10));
        info.setBackground(new Color(94, 133, 197));
        panel.add(info, BorderLayout.NORTH);

        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        bottomPanel.setBackground(new Color(94, 133, 197));
        panel.add(bottomPanel, BorderLayout.CENTER);

        JLabel label = new JLabel("Enter Exam ID:");
        label.setFont(new Font("Arial", Font.ITALIC, 12));
        info.add(label);

        info.add(new JLabel());

        JTextField examId = new JTextField();
        info.add(examId);

        for(String title: new String[] {"ID", "Name", "Grade"}){
            JLabel header = new JLabel(title);
            header.setForeground(Color.ORANGE);
            header.setFont(new Font("Verdana", Font.BOLD, 15));
            info.add(header);
        }

        for(Student student: course.getStudents()){
            JLabel idLabel = new JLabel(student.getId());
            JLabel nameLabel = new JLabel(student.getName());

            idLabel.setFont(new Font("Arial", Font.PLAIN, 12));
            nameLabel.setFont(new Font("Arial", Font.PLAIN, 12));

            info.add(idLabel);
            info.add(nameLabel);
            JTextField grade = new JTextField();
            grades.add(grade);
            info.add(grade);
        }

        JButton saveButton = new JButton("Save");
        bottomPanel.add(saveButton);

        JSaveGrades saveListener = new JSaveGrades(course, instructor, examId, grades, refresher);
        saveButton.addActionListener(saveListener);

        panel.revalidate();
        panel.repaint();
    }
}
