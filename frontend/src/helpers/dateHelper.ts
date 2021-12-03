const months: string[] = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

/**
 * Displays date in more readable form.
 * @param date date string in the form {Year}-{Month}-{Day}
 * @returns Date string in the form {Month short name} {Day} {Year}
 * @throws {InvalidMonthError} when Month value is not between 1 to 12.
 */
export function displayDateString (date: string): string {
  try {
    const [year, month, day] = date.split('-')
    const monthInd: number = Number.parseInt(month)
    if (monthInd < 1 || monthInd > 12) {
      throw new InvalidMonthError('Month value must be between 1-12 was given: '.concat(month))
    }
    return months[monthInd - 1] + ' ' + day + ' ' + year
  } catch (err) {
    console.error('Encountered error: '.concat((err as Error).message))
    throw err
  }
}

export class InvalidMonthError extends Error {}
