import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Task {
  final String name;
  final String description;
  final DateTime dueDate;

  Task({required this.name, required this.description, required this.dueDate});

  factory Task.fromJson(Map<String, dynamic> json) {
    return Task(
      name: json['firstname'] + ' ' + json['lastname'],
      description: json['email'],
      dueDate: DateTime.now().add(Duration(days: json['age'])),
    );
  }
}

class TaskListPage extends StatefulWidget {
  @override
  _TaskListPageState createState() => _TaskListPageState();
}

class _TaskListPageState extends State<TaskListPage> {
  late Future<List<Task>> futureTasks;

  @override
  void initState() {
    super.initState();
    futureTasks = fetchTasks();
  }

  Future<List<Task>> fetchTasks() async {
    final response = await http.get(Uri.parse('http://localhost:5000/api/users'));

    if (response.statusCode == 200) {
      List jsonResponse = json.decode(response.body);
      return jsonResponse.map((task) => Task.fromJson(task)).toList();
    } else {
      throw Exception('Failed to load tasks');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Task List'),
      ),
      body: FutureBuilder<List<Task>>(
        future: futureTasks,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return Center(child: Text('No tasks found'));
          } else {
            return ListView.builder(
              itemCount: snapshot.data!.length,
              itemBuilder: (context, index) {
                final task = snapshot.data![index];
                return ListTile(
                  title: Text(task.name),
                  subtitle: Text('${task.description}\nDue: ${task.dueDate}'),
                );
              },
            );
          }
        },
      ),
    );
  }
}