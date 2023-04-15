package gui;

import model.Course;
import model.Student;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class JListGrades implements ActionListener {
    private JPanel panel;
    private  Course course;

    public JListGrades(JPanel panel, Course course){
        this.panel = panel;
        this.course = course;
    }

    public void actionPerformed(ActionEvent e) {
        if(course.getStudents().size() == 0){
            JOptionPane.showMessageDialog(null, "There are no students taking this course!");
            return;
        }

        panel.removeAll();
        panel.setBackground(new Color(94, 133, 197));
        panel.setLayout(new BorderLayout());

        int examCount = course.getStudents().get(0).listExamID(course.getId()).size();

        JPanel info = new JPanel(new GridLayout(examCount*(course.getStudents().size()+2), 3));
        info.setBackground(new Color(94, 133, 197));
        panel.add(info, BorderLayout.NORTH);

        for(String examID: course.getStudents().get(0).listExamID(course.getId())){
            for (String title : new String[]{"ID", "Name", examID}) {
                JLabel header = new JLabel(title);
                header.setForeground(Color.ORANGE);
                header.setFont(new Font("Verdana", Font.BOLD, 15));
                info.add(header);
            }

            float totalGrade = 0;

            for(Student student: course.getStudents()){
                JLabel idLabel = new JLabel(student.getId());
                JLabel nameLabel = new JLabel(student.getName());
                JLabel gradeLabel = new JLabel(String.valueOf(student.getGradeItem(course.getId(), examID).getGrade()));

                idLabel.setFont(new Font("Arial", Font.PLAIN, 12));
                nameLabel.setFont(new Font("Arial", Font.PLAIN, 12));
                gradeLabel.setFont(new Font("Arial", Font.PLAIN, 12));

                info.add(idLabel);
                info.add(nameLabel);
                info.add(gradeLabel);
                totalGrade += student.getGradeItem(course.getId(), examID).getGrade();
            }

            for (String title : new String[]{"Average", "", String.valueOf(totalGrade/course.getStudents().size())}) {
                JLabel average = new JLabel(title);
                average.setForeground(Color.WHITE);
                average.setFont(new Font("Verdana", Font.BOLD, 14));
                info.add(average);
            }
        }
        panel.revalidate();
        panel.repaint();
    }
}
