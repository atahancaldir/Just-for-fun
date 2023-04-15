package gui;

import model.Course;
import model.Student;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class JListStudents implements ActionListener {
    private JPanel panel;
    private Course course;

    public JListStudents(JPanel panel, Course course){
        this.panel = panel;
        this.course = course;
    }

    public void actionPerformed(ActionEvent e) {
        panel.removeAll();
        panel.setBackground(new Color(94, 133, 197));
        panel.setLayout(new BorderLayout());

        JPanel info = new JPanel(new GridLayout(course.getStudents().size()+1, 3));
        info.setBackground(new Color(94, 133, 197));
        panel.add(info, BorderLayout.NORTH);

        for(String title: new String[] {"ID", "Name", "Email"}){
            JLabel header = new JLabel(title);
            header.setForeground(Color.ORANGE);
            header.setFont(new Font("Verdana", Font.BOLD, 15));
            info.add(header);
        }

        for(Student student: course.getStudents()){
            JLabel idLabel = new JLabel(student.getId());
            JLabel nameLabel = new JLabel(student.getName());
            JLabel emailLabel = new JLabel(student.getEmail());

            idLabel.setFont(new Font("Arial", Font.PLAIN, 12));
            nameLabel.setFont(new Font("Arial", Font.PLAIN, 12));
            emailLabel.setFont(new Font("Arial", Font.PLAIN, 12));

            info.add(idLabel);
            info.add(nameLabel);
            info.add(emailLabel);
        }

        panel.revalidate();
        panel.repaint();
    }
}
