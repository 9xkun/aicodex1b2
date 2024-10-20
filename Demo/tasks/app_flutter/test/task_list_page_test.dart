import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:app_flutter/task_list_page.dart';

@GenerateMocks([http.Client])
void main() {
  group('TaskListPage', () {
    testWidgets('displays a loading indicator while fetching tasks', (WidgetTester tester) async {
      final client = MockClient();

      when(client.get(Uri.parse('http:/localhost:5000/api/users')))
          .thenAnswer((_) async => http.Response('[]', 200));

      await tester.pumpWidget(MaterialApp(
        home: TaskListPage(),
      ));

      expect(find.byType(CircularProgressIndicator), findsOneWidget);
    });

    testWidgets('displays an error message if the task fetching fails', (WidgetTester tester) async {
      final client = MockClient();

      when(client.get(Uri.parse('http:/localhost:5000/api/users')))
          .thenAnswer((_) async => http.Response('Not Found', 404));

      await tester.pumpWidget(MaterialApp(
        home: TaskListPage(),
      ));

      await tester.pump(); // Rebuild the widget with the error

      expect(find.text('Failed to load tasks'), findsOneWidget);
    });

    testWidgets('displays a list of tasks when the fetching is successful', (WidgetTester tester) async {
      final client = MockClient();

      final mockResponse = jsonEncode([
        {
          'firstname': 'John',
          'lastname': 'Doe',
          'email': 'john.doe@example.com',
          'age': '2023-10-01T00:00:00.000Z'
        },
        {
          'firstname': 'Jane',
          'lastname': 'Smith',
          'email': 'jane.smith@example.com',
          'age': '2023-11-01T00:00:00.000Z'
        }
      ]);

      when(client.get(Uri.parse('http:/localhost:5000/api/users')))
          .thenAnswer((_) async => http.Response(mockResponse, 200));

      await tester.pumpWidget(MaterialApp(
        home: TaskListPage(),
      ));

      await tester.pump(); // Rebuild the widget with the fetched data

      expect(find.text('John Doe'), findsOneWidget);
      expect(find.text('jane.smith@example.com'), findsOneWidget);
    });
  });
}