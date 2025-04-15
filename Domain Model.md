| Entity       | Attributes                              | Methods                        | Relationships                          |

|--------------|-----------------------------------------|--------------------------------|----------------------------------------|

| GBV Case     | caseId: String                          | assignCase()                   | Associated with User                   |

|              | status: String                          | reviewCase()                   | Managed by Clinic Staff                |

|              | reportedDate: Date                      | escalateCase()                 |                                        |

|              | resolvedDate: Date                      | resolveCase()                  |                                        |

|--------------|-----------------------------------------|--------------------------------|----------------------------------------|

| User Account | userId: String                          | activateAccount()              | Can report GBV Case                    |

|              | name: String                            | suspendAccount()               | Can receive Notifications              |

|              | email: String                           | deactivateAccount()            |                                        |

|              | status: String                          |                                |                                        |

|--------------|-----------------------------------------|--------------------------------|----------------------------------------|

| Notification | notificationId: String                  | sendNotification()             | Sent to User Account                   |

|              | type: String                            | markAsRead()                   |                                        |

|              | sentDate: Date                          |                                |                                        |

|              | readDate: Date                          |                                |                                        |

|--------------|-----------------------------------------|--------------------------------|----------------------------------------|

| Report       | reportId: String                        | submitReport()                 | Created by User Account                |

|              | title: String                           | approveReport()                | Reviewed by Admin                      |

|              | content: String                         | rejectReport()                 |                                        |

|              | status: String                          |                                |                                        |

|--------------|-----------------------------------------|--------------------------------|----------------------------------------|

| Appointment  | appointmentId: String                   | scheduleAppointment()          | Scheduled by User Account              |

|              | date: Date                              | confirmAppointment()           | Managed by Clinic Staff                |

|              | time: String                            | cancelAppointment()            |                                        |

|              | status: String                          |                                |                                        |

|--------------|-----------------------------------------|--------------------------------|----------------------------------------|

| Feedback     | feedbackId: String                      | submitFeedback()               | Submitted by User Account              |

|              | content: String                         | reviewFeedback()               | Reviewed by Admin                      |

|              | submittedDate: Date                     | addressFeedback()              |                                        |

|              | status: String                          |                                |                                        |

|--------------|-----------------------------------------|--------------------------------|----------------------------------------|

| Incident     | incidentId: String                      | reportIncident()               | Reported by User Account               |

|              | description: String                     | investigateIncident()          | Investigated by Security Personnel     |

|              | reportedDate: Date                      | resolveIncident()              |                                        |

|              | status: String                          |                                |                                        |

|--------------|-----------------------------------------|--------------------------------|----------------------------------------|

| Task         | taskId: String                          | startTask()                    | Assigned to Clinic Staff               |

|              | description: String                     | completeTask()                 |                                        |

|              | status: String                          | blockTask()                    |                                        |

|              | assignedTo: String                      |                                |                                        |
