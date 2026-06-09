import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ParallelRouteOptimizationDemo {

    public static void main(String[] args) {
        List<String> routes = Arrays.asList(
                "Hat 23 - Üniversite Merkez",
                "Hat 45 - Otogar Merkez",
                "Hat 12 - Hastane Merkez",
                "Hat 18 - Sanayi Merkez",
                "Hat 30 - Çarşı Kampüs"
        );

        ExecutorService executor = Executors.newFixedThreadPool(3);

        System.out.println("Rota optimizasyon işlemleri başlatıldı...\n");

        for (String route : routes) {
            executor.submit(() -> optimizeRoute(route));
        }

        executor.shutdown();
    }

    private static void optimizeRoute(String routeName) {
        try {
            System.out.println(routeName + " için optimizasyon başladı. Thread: "
                    + Thread.currentThread().getName());

            // Burada gerçek projede trafik yoğunluğu, mesafe ve yolcu talebi hesaplanır.
            Thread.sleep(2000);

            System.out.println(routeName + " için en uygun rota hesaplandı.");
        } catch (InterruptedException e) {
            System.out.println(routeName + " optimizasyonu kesintiye uğradı.");
            Thread.currentThread().interrupt();
        }
    }
}
