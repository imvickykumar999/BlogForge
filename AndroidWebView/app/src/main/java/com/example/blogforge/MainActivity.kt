package com.example.blogforge

import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.OnBackPressedCallback
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import com.example.blogforge.ui.theme.BlogForgeTheme

class MainActivity : ComponentActivity() {
    private lateinit var webView: WebView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        // Back button handling
        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (webView.canGoBack()) {
                    webView.goBack()
                } else {
                    finish() // If no more history, finish the activity
                }
            }
        })

        setContent {
            BlogForgeTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    WebViewContainer(
                        modifier = Modifier.padding(innerPadding)
                    ) { webViewInstance ->
                        webView = webViewInstance
                    }
                }
            }
        }
    }
}

@Composable
fun WebViewContainer(modifier: Modifier = Modifier, onWebViewCreated: (WebView) -> Unit) {
    // URL of the website you want to display
    val websiteUrl = "https://blogforge.pythonanywhere.com/" // Replace with your URL

    AndroidView(
        factory = { context ->
            WebView(context).apply {
                settings.javaScriptEnabled = true
                settings.domStorageEnabled = true // Enable DOM storage if needed
                webViewClient = WebViewClient()
                loadUrl(websiteUrl)
            }
        },
        modifier = modifier,
        update = {
            onWebViewCreated(it)
        }
    )
}
