package higher_order

import utils.Display

import scala.annotation.tailrec
import scala.util.{Failure, Success, Try}

object Simple {
  def compute(f: (Int, Int) => Int, a: Int, b: Int): Int = f(a, b)
}

object Time {
  def timer[A](f: => A): A = {
    val startTime = System.nanoTime
    val result = f
    val endTime = System.nanoTime
    println(s"Execution took ${endTime - startTime} nano seconds.")
    result
  }
}
object Retry {
  @tailrec
  def retry[A](nbRetries: Int)(f: => A): Try[A] = {
    Try(f) match {
      case Success(x) => Success(x)
      case _ if nbRetries > 1 => retry(nbRetries - 1)(f)
      case Failure(e) => Failure(e)
    }
  }
}

object ListTransformation {
  @tailrec
  def transformSeq[A](list: List[A], fns: Seq[A => A]): List[A] = fns match {
    case Seq() => list
    case fn +: remainingFns => transformSeq(list.map(fn), remainingFns)
  }
}

object Higher extends App with Display {

  def sum(a: Int, b: Int): Int = a + b
  def multiple(a: Int, b: Int): Int = a * b

  val exos = Seq(
    Simple.compute(sum, 1, 2),
    Simple.compute(multiple, 1, 2),
    Time.timer(sum(1, 2)),
    Retry.retry(3)(sum(2, 2))
  )
  exos.foreach(res => res.show())

  val numbers = List(1, 2, 3)
  val fns = Seq((x: Int) => x + 1, (x: Int) => x * 2)
  val result = ListTransformation.transformSeq(numbers, fns)
  result.show()
}
