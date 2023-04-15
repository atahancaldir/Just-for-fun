package model;

public abstract class Person {
    private String id = "";
    private String name;
    private String email;
    private static int idCounter = 0;

    public Person(String name) {
        this.name = name;
        idCounter++;

        String[] splittedName = this.name.split(" ");
        id += splittedName[0].charAt(0); //first letter of name
        id += splittedName[1].charAt(0); //first letter of surname
        id += String.format("%04d", idCounter); //adding counter value as a 4 digit number
    }

    public abstract void initEmail();

    public String getId() {
        return id.toLowerCase();
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
