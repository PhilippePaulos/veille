package nomades

import scala.util.{Try, Success, Failure}

object Test extends App {

  // Option

  val input: Option[String] = Some("42")
  var result1 = input.map(_.toInt).getOrElse(0)
  println(result1) // Output: 42

  val input2: Option[String] = None
  val result2 = input2.map(_.toInt).getOrElse(0)
  println(result2) // Output: 0


  // Try

  def divide(dividend: Int, divisor: Int): Try[Int] = {
    Try(dividend / divisor)
  }

  val result3 = divide(10, 0)
  result3 match {
    case Success(value) => println(s"Result: $value")
    case Failure(exception) => println(s"Error: $exception")
  }

  // Future
  import scala.concurrent.Future
  import scala.concurrent.ExecutionContext.Implicits.global

  def longComputation(x: Int): Future[Int] = {
    Future {
      Thread.sleep(1000)
      x * 2
    }
  }

  val result4 = for {
    a <- longComputation(1)
    b <- longComputation(2)
    c <- longComputation(3)
  } yield a + b + c

  result4 onComplete {
    case Success(value) => println(s"Result: $value")
    case Failure(exception) => println(s"Error: $exception")
  }

  val option1: Option[String] = Some("1")
  var option2: Option[String] = Some("2")
//  option2 = None

  val result5 = for {
    a <- option1
    b <- option2
  } yield a + b

  result5.foreach(sum => println(s"The sum is $sum"))




}
